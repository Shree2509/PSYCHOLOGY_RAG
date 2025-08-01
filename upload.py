from langchain_community.document_loaders import PyPDFLoader
from qdrant_client import QdrantClient
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

file_path = "D:/bhuvi/New_folder/rag/psychology.pdf"
loader = PyPDFLoader(file_path)
data = loader.load_and_split()


embeddings = OllamaEmbeddings(model="llama3.2:1b")

url=""
api_key=""




qdrant = QdrantVectorStore.from_documents(
    data,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="psychology",
)