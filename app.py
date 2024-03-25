from langchain.chains import RetrievalQA
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
import chainlit as cl
from pipeline.rag import RAGPipeline
from pipeline.llm import LLM


rag = RAGPipeline()
llm = LLM().get_llm()


@cl.on_chat_start
async def on_chat_start():
    files = None
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a file to begin!",
            accept=["text/plain", "text/csv", "application/pdf"],
            max_size_mb=100,
            timeout=600,
        ).send()

    file = files[0]

    msg = cl.Message(content=f"Processing `{file.name}`...")
    await msg.send()

    retriever = rag.create_retriever(file.path)
    message_history = ChatMessageHistory()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="result",
        chat_memory=message_history,
        return_messages=True,
    )
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
    )

    # Let the user know that the system is ready
    msg.content = (
        f"Processing `{file.name}` done. \n Hi, Welcome to Chat With Documents!"
    )
    await msg.update()

    cl.user_session.set("qa", qa)


@cl.on_message
async def main(message: cl.Message):
    qa = cl.user_session.get("qa")
    cb = cl.AsyncLangchainCallbackHandler()

    res = await qa.ainvoke(message.content, callbacks=[cb])

    answer = res["result"]
    source_documents = res["source_documents"]

    text_elements = []

    if source_documents:
        for source_idx, source_doc in enumerate(source_documents):
            source_name = f"source_{source_idx}"
            # Create the text element referenced in the message
            text_elements.append(
                cl.Text(content=source_doc.page_content, name=source_name)
            )
        source_names = [text_el.name for text_el in text_elements]

        if source_names:
            answer += f"\nSources: {', '.join(source_names)}"
        else:
            answer += "\nNo sources found"

    await cl.Message(content=answer, elements=text_elements).send()
