'''
Created on 18 Jun 2025

@author: User
'''



from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
import getpass

print("Working started")


from google import genai

client = genai.Client(api_key="<<API Key>>")

result = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents="What is the meaning of life?")

print(result.embeddings)