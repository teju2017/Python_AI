'''
Created on 16 Jun 2025

@author: User
'''
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import openai
from langchain.chains import retrieval_qa
from langchain.document_loaders import TextLoader
from langchain.chains.retrieval_qa.base import VectorDBQA


loader = TextLoader('P:\GITPROJECTS\PythonProjects\state_of_the_union.txt')
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

persist_directory = 'db'

embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=texts, embedding=embedding, persist_directory=persist_directory)


'''
vectordb=Chroma.from_document(Chroma.from_documents(documents=texts, embedding=embedding)
'''






'''
qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vectordb)
'''

        
    
    
    
   


    
       
        