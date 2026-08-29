from benchmark.benchmark import Benchmark

from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

embedder = SentenceTransformerEmbedder()

texts = [

    "Artificial Intelligence"

] * 100


Benchmark.run(

    "Embedding Benchmark",

    embedder.embed,

    texts

)