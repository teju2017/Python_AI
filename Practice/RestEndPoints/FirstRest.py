'''
Created on 27 Jun 2025

@author: User
'''

from fastapi import FastAPI
from RestEndPoints import QueryVectorPdf
from fastapi import FastAPI, File, UploadFile
from RestEndPoints import Utility
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os
from chromadb.test.test_api import persist_dir
from langchain_community.utilities.pebblo import file_loader

app = FastAPI(
    title="Awesome API",
    description="An API that does awesome stuff",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "url": "https://yourwebsite.com",
        "email": "you@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

os.environ["GOOGLE_API_KEY"] = "AIzaSyBDxJgLH-tN1cxGZYzPGq0bvtLvwYFY80w"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "AIzaSyBDxJgLH-tN1cxGZYzPGq0bvtLvwYFY80w"


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{prompt_message}")
async def checkItems(prompt_message):
    return QueryVectorPdf.run_the_query(prompt_message)    
    


@app.post("/upload-pdf/")
async def upload_pdf(pdf_file: UploadFile = File(...)):
   if(pdf_file.filename.endswith("pdf")):
     file_location = f"temp_{pdf_file.filename}"
     with open(file_location, "wb") as buffer:
            buffer.write(await pdf_file.read())
     loader = PyPDFLoader(file_location)
     pages= loader.load_and_split()
     text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50,separators=["\n","\n\n","\r"])
     chunks = text_splitter.split_documents(pages)
     vector_store = Chroma(
      collection_name="Collection_pdf",
      embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
      persist_directory="P:\\chroma",  # Where to save data locally, remove if not necessary
     )
     print(vector_store.add_documents(documents=chunks))
     return vector_store.__sizeof__()
    
@app.post("/upload-txt/")
async def upload_text(txt_file: UploadFile = File(...)):
   if(txt_file.filename.endswith("txt")):
     file_location = f"temp_{txt_file.filename}"
     with open(file_location, "wb") as abc:
         abc.write(await txt_file.read())
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


@app.put("/PurgeData")
async def clean_Collection():
    vector_store = Chroma(
    collection_name="Collection_pdf",
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
    persist_directory="P:\\chroma",  # Where to save data locally, remove if not necessary
    )
    vector_store.reset_collection()
    Utility.clean_directory("P:\\chroma\\")
        
@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Custom Swagger UI",
        swagger_favicon_url="https://example.com/favicon.png",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css"
    )
    