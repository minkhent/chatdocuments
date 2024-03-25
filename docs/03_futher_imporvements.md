# Futher Improvements
This is a theoritical side note to improve RAG systems.Naive RAG faces significant challenges in two key areas: “Retrieval,” and  “Generation”.


Retrieval quality poses diverse challenges, including low precision, leading to misaligned retrieved chunks and potential issues like hallucination.
## Retrieval Improvements

- Chunk optimization( semantic chunking )
- Fine-tuning Embedding Models

1. ###### Aligning Queries and Documents
    - Query Rewriting
    - Embedding Transformation

2. ###### Aligning Retriever and LLM
    - Fine-tuning Retrievers
    - Adapters

Generation quality presents hallucination challenge, where the model generates answers not grounded in the provided context, as well as issues of irrelevant context and potential toxicity or bias in the model’s output.
## Generation Improvements

1. ###### Post-retrieval with Frozen LLM
    - Information Compression
    - Reranking

2. ###### Fine-tuning LLM for RAG


# Evaluation Benchmarks and Tools

1. ## Benchmarks
    1. Answer Relevance (evaluate the relevance of retrieval)
    2. Faithfulness (evaluate the quality of answers )
    3. Context Relevance ( evaluate the quality of retrieval)
    5. Noise Robustness ( the model’s capability to man-age noise documents that are question-related)
    6. Counterfactual Robustness (tests the model’s ability to recognize known inaccuracies within documents)

2. ## Evaluation Tools
    1. [ARES](https://github.com/stanford-futuredata/ARES)
    2. [TruLens](https://github.com/truera/trulens)
    3. [RAGAS] (https://github.com/explodinggradients/ragas)
