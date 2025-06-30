'''
Created on 25 Jun 2025

@author: User
'''

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from urllib3.util.request import ChunksAndContentLength
import os




os.environ["GOOGLE_API_KEY"] = "AIzaSyBDxJgLH-tN1cxGZYzPGq0bvtLvwYFY80w"
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


loader = PyPDFLoader("P:\\books\\serverless-architectures-with-aws-lambda.pdf")
pages= loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(pages)


vector_store = Chroma(
    collection_name="Collection_pdf",
    embedding_function=embeddings,
    persist_directory="P:\\chroma",  # Where to save data locally, remove if not necessary
    )



vector_store.add_documents(documents=chunks)
vector_store=Chroma.from_documents(documents=chunks, embedding=embeddings)




print("Size of vector store "+str(vector_store._collection.count()))

results=vector_store.similarity_search("what is odwek",1)
print(results[0].page_content)