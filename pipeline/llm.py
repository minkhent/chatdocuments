import os
import time
from dotenv import load_dotenv
from langchain_community.llms import LlamaCpp


load_dotenv()


class LLM:
    def __init__(self) -> None:
        self.local_model_path = os.getenv("MODEL_PATH")

    def get_llm(self) -> LlamaCpp:

        start = time.time()

        llm = LlamaCpp(
            model_path=self.local_model_path,
            verbose=False,
            n_ctx=4098,
        )
        end = time.time()
        print("Time to load the model:", end - start)
        return llm
