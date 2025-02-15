from adalflow import OpenAIClient


configs = {
    "embedder": {
        "batch_size": 100,
        "model_client": OpenAIClient,  # make sure to initialize the model client later
        "model_kwargs": {
            "model": "text-embedding-3-small",
            "dimensions": 256,
            "encoding_format": "float",
        },
    },
    "retriever": {
        "top_k": 20,
    },
    "generator": {
        "model_client": OpenAIClient,
        "model_kwargs": {
            "model": "gemini-2.0-flash",
            "temperature": 0.3,
            "stream": False,
        },
    },
    "text_splitter": {
        "split_by": "word",
        "chunk_size": 400,
        "chunk_overlap": 100,
    },
}

DEFAULT_GITHUB_REPO = "https://github.com/SylphAI-Inc/AdalFlow"
