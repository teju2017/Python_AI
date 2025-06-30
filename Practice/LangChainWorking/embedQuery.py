'''
Created on 17 Jun 2025

@author: User
'''


import getpass
import os
from langchain_chroma import Chroma
import chromadb
from uuid import uuid4

from langchain_core.documents import Document


def workingTest():
  if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Please pass the API")

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

list_of_vector_float=embeddings.embed_query("Hello, world!")
print(list_of_vector_float)



