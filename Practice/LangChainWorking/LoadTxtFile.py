'''
Created on 29 Jun 2025

@author: User
'''

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import io

import os
from langchain_core.documents import Document
from turtledemo.chaos import line
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader



def test():
 os.environ["GOOGLE_API_KEY"] = "AIzaSyBDxJgLH-tN1cxGZYzPGq0bvtLvwYFY80w"
 vector_store = Chroma(
      collection_name="Collection_pdf",
      embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
      persist_directory="P:\\chroma",  # Where to save data locally, remove if not necessary
     )
 file = open('C:\\Users\\User\\Downloads\\state_of_the_union.txt', encoding="utf8")
 content=file.readlines()
 list_of_documents=[]
 print(content)
 file.close()
 counter=0
 for line in content:
    counter=counter+1
    val=str(counter)
    var="document_"+val  
    var=Document("page_content= "+line+" ,"+"id ="+val)
    print(f'{var}')
    list_of_documents.append(line)
 print(list_of_documents)
 vector_store.add_documents(documents=list_of_documents)
 vector_store.similarity_search("tell me about this text file", 1)


def work():
    file_location="C:\\Users\\User\\Downloads\\state_of_the_union.txt"
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBDxJgLH-tN1cxGZYzPGq0bvtLvwYFY80w"
    loader = TextLoader(file_location,encoding="utf8")
        
        
    
    pages= loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50,separators=["\n","\n\n","\r"])
    chunks = text_splitter.split_documents(pages)
    vector_store = Chroma(
      collection_name="Collection_pdf",
      embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
      persist_directory="P:\\chroma",  # Where to save data locally, remove if not necessary
     )
    print(vector_store.add_documents(documents=chunks))
    return vector_store.__sizeof__() 

work()
    

