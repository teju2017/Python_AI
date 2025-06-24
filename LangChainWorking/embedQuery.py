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



if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("AIzaSyCgXw_zpkCoV47w0nvEP5sD9P03IUvjFVw")

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

embeddings.embed_query("Hello, world!")


