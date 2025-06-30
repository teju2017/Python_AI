'''
Created on 19 Jun 2025

@author: User
'''

from langchain_google_genai import google_vector_store
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai
from google.ai.generativelanguage_v1alpha.types import retriever
import os
import getpass
from langchain_community.vectorstores import FAISS
from LangChainWorking.LaodChroma import vector_store
from langchain_chroma import  Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader




print("Program to use vectorstore")


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

loader=TextLoader("abc.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = GoogleGenerativeAIEmbeddings()
vectorstore = FAISS.from_documents(texts, embeddings)


retriever=vector_store.as_retriever()
docs = retriever.invoke("Tell me the stock price")

