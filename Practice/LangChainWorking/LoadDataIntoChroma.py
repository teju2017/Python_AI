'''
Created on 20 Jun 2025

@author: User
'''



import getpass
import os
import chromadb
from langchain_chroma.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import chromadb
from uuid import uuid4
from langchain_core.documents import Document
from LangChainWorking.LaodChroma import vector_store





if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass('Please pass the API')

  

    

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")





vector_store = Chroma(
    collection_name="Collection_new",
    embedding_function=embeddings,
    persist_directory="P:\\chroma",  # Where to save data locally, remove if not necessary
)










document_1 = Document(
    page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
    id=1,
)

document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
    id=2,
)

document_3 = Document(
    page_content="Building an exciting new project with LangChain - come check it out!",
    metadata={"source": "tweet"},
    id=3,
)

document_4 = Document(
    page_content="Robbers broke into the city bank and stole $1 million in cash.",
    metadata={"source": "news"},
    id=4,
)

document_5 = Document(
    page_content="Wow! That was an amazing movie. I can't wait to see it again.",
    metadata={"source": "tweet"},
    id=5,
)

document_6 = Document(
    page_content="Is the new iPhone worth the price? Read this review to find out.",
    metadata={"source": "website"},
    id=6,
)

document_7 = Document(
    page_content="The top 10 soccer players in the world right now.",
    metadata={"source": "website"},
    id=7,
)

document_8 = Document(
    page_content="LangGraph is the best framework for building stateful, agentic applications!",
    metadata={"source": "tweet"},
    id=8,
)

document_9 = Document(
    page_content="The stock market is down 500 points today due to fears of a recession.",
    metadata={"source": "news"},
    id=9,
)

document_10 = Document(
    page_content="I have a bad feeling I am going to get deleted :(",
    metadata={"source": "tweet"},
    id=10,
)

document_11 = Document(
    page_content="OMS stands for Output management system",
    metadata={"source": "tweet"},
    id=11,
)

document_12 = Document(
    page_content="Gill is the Indian test team captain",
    metadata={"source": "tweet"},
    id=12,
)

document_13 = Document(
            page_content="No alternative for hard work to attain perfection in any new skill",
            metadata={"source": "tweet"},
            id=13,
)

documents = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11,
    document_12,
    document_13
]

print(documents)

print("Loading data into")
uuids = [str(uuid4()) for _ in range(len(documents))]

print("Size of DOcuments is "+str(documents.__sizeof__()))

vector_store.add_documents(documents=documents)

print("Collection name ="+vector_store._collection_name)



query="Test Captian"
print("Question is "+query)
results=vector_store.similarity_search(query,1)
print(results)



