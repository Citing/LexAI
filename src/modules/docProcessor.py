from langchain_text_splitters import RecursiveCharacterTextSplitter
from modules.config import Config
from modules.ai import embedding
import streamlit as st

class docProcessor:
    def __init__(self, vectorDB):
        self.__vectorDB = vectorDB

    def docProcess(self, fileName, content):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False,
        )
        texts = text_splitter.split_text(content)
        embeddings = [embedding(text) for text in texts]
        st.write(len(embeddings))
        # ids = list(range(len(texts)))
        # self.__vectorDB.docInsert(embeddings, fileName, texts, ids)
        # st.write("docProcess")
        
    def get_all_documents(self):
        return