from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from llm import completion_prompt


embeddings = OllamaEmbeddings(model="llama3.2:1b")

url="https://333d6f8e-03f2-49ce-b1e2-0888d033f7ca.eu-central-1-0.aws.cloud.qdrant.io:6333"
api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.haQlJ0ubKtRTKLvU48xtNfLJeJJQS-s2jgSlmi1md48"

question=input("Enter your question: ")

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="psychology",
    url=url,
    api_key=api_key,
)

response = qdrant.similarity_search(
    question,k=2
)
print(response)


prompt= f"""
Question: {question}

context: {response}

you are a helpful assistant that can answer questions about the context provided.

"""
print("prompt: ",prompt)
completion_prompt(prompt)