# System improvements
This is practical improvements for RAG system in both latency and accuracy.

1. ## Using semantic cache 
    Latency and Cost are significant hurdles for developers building on top of Language Models. High latency can degrade the user experience, and increased costs can impact scalability.Caching allows you to efficiently reuse previously retrieved or computed data.
    - [GPTCache](https://github.com/zilliztech/GPTCache)
    - Redis
    - Mongo 


2. ## Using semantic chunking
    Most commonly used chunking methods are rule-based, employing techniques such as fixed chunk size or overlap of adjacent chunks. Semantic chunking aims to ensure that each chunk contains as much semantically independent information as possible.
    - [link](https://www.youtube.com/watch?v=8OJC21T2SL4)
    - [langchain docs](https://python.langchain.com/docs/modules/data_connection/document_transformers/semantic-chunker)

3. ## Using different LLM backend 
    - [tensorRT_LLM](https://github.com/triton-inference-server/tensorrtllm_backend)
    - [vllm](https://github.com/vllm-project/vllm)
    - [hg-inference engine](https://github.com/huggingface/text-generation-inference)https://github.com/deepset-ai/haystack
    -[haystack](https://github.com/deepset-ai/haystack)

5. ## Using Monitroing/observability system
    - [langfuse](https://langfuse.com/)
    - [uptrain](https://github.com/uptrain-ai/uptrain)
    - [phoenix](https://github.com/Arize-ai/phoenix)

6. ## Analysis on sematic search
    - [chromaviz](https://github.com/mtybadger/chromaviz)
    - [pgvector](https://github.com/pgvector/pgvector)
    - [vector-admin](https://github.com/Mintplex-Labs/vector-admin)

7. ## Using reranker model
    - [bge-reranker](https://huggingface.co/BAAI/bge-reranker-large)
    - [flashrank-reranker](https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker)

8. ## Using Agentic action
    - [autogen](https://github.com/microsoft/autogen)
    - [crewAI](https://github.com/joaomdmoura/crewAI)
    - [ReactAgent](https://towardsdatascience.com/using-langchain-react-agents-for-answering-multi-hop-questions-in-rag-systems-893208c1847e)
9. ## Using Knowledge graph
    - [reference](https://neo4j.com/developer-blog/graph-llm-rag-application-pdf-documents/)
