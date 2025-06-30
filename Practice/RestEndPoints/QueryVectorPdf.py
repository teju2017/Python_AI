'''
Created on 25 Jun 2025

@author: User
'''

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os


def run_the_query(prompt_query):
    os.environ["GOOGLE_API_KEY"] = ""
    os.environ["GOOGLE_API_KEY"] = ""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = Chroma(
    collection_name="Collection_pdf",
    embedding_function=embeddings,
    persist_directory="P:\\chroma",  # Where to save data locally, remove if not necessary
    )
    print("Size of vector store "+str(vector_store._collection.count()))
    results=vector_store.similarity_search(prompt_query,1)
    if(len(results) > 0):
      return results[0].page_content.split("\n")
    else:
      return "message:No data available in collection to respond" 

  

    
    


