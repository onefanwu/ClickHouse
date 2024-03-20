import torch
from sentence_transformers import SentenceTransformer


if torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using GPU:", torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")
    print("Using CPU")

model_path = '/workdir/AiQ-dev/models/all-MiniLM-L6-v2'
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', cache_folder='/workdir/AiQ-dev/models')
model = SentenceTransformer(model_path, device=device)

sentences = [
    "This is an example sentence",
    "Each sentence is converted into a fixed-sized vector"
]

embeddings = model.encode(sentences)

# for sentence, embedding in zip(sentences, embeddings):
#     print("Sentence:", sentence)
#     print("Embedding:", embedding)
#     print("")

from sklearn.metrics.pairwise import cosine_similarity

similarity_scores = cosine_similarity(
    [embeddings[0]],
    embeddings[1:] 
)

print("Similarity to the first sentence:")
for i, score in enumerate(similarity_scores[0], start=1):
    print(f"Sentence {i+1}: {score}")