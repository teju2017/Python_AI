'''
Created on 18 Jun 2025

@author: User
'''


import getpass
import os


from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document


os.environ["GOOGLE_API_KEY"] = ""
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store = Chroma(
    collection_name="Collection_new",
    embedding_function=embeddings,
    persist_directory="P:\\chroma",  # Where to save data locally, remove if not necessary
)

document_13 = Document(
            page_content="No alternative for hard work to attain perfection in any new skill",
            metadata={"source": "tweet"},
            id=13)


document_14 = Document(
            page_content="Avyukth is in K1 class",
            metadata={"source": "tweet"},
            id=14)


document_15 = Document(
            page_content="Hackathon is a must for aspiring developers to push their limits",
            metadata={"source": "tweet"},
            id=15)


document=[document_13,document_14,document_15]

vector_store.add_documents(documents=document)

query="what does a software engineer should do"
print("Question is : "+query)
results=vector_store.similarity_search(query,1)
print(results[0])
