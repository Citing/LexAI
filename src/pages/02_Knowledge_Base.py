import streamlit as st
from modules.milvusDB import MilvusDB
from modules.docProcessor import docProcessor
from css.layout import set_header

set_header("Knowledge Base")

vectorDB = MilvusDB()
vectorDB.collectionCreate()
docProcessor = docProcessor(vectorDB)

vectorDB.list_all_filenames()

fileUpload = st.file_uploader("Upload a document", type=["txt"])
if fileUpload is not None:
    content = fileUpload.read().decode("utf-8")
    docProcessor.docProcess(fileUpload.name, content)
    st.success(f"Document {fileUpload.name} processed and stored in the knowledge base!")

