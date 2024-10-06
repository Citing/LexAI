from pymilvus import (
    connections, FieldSchema, CollectionSchema, DataType,
    Collection, utility
)
import numpy as np
import streamlit as st
from modules.config import Config

class MilvusDB:
    def __init__(self, collectionName='knowledgeBase'):
        self.__collectionName = collectionName
        self.__host = Config.MILVUS_HOST
        self.__port = Config.MILVUS_PORT
        self.connect()

    def connect(self):
        connections.connect("default", host=self.__host, port=self.__port, db_name="LegalKnowledge")

    def collectionCreate(self, vector_dim=1536):
        if not utility.has_collection(self.__collectionName):
            fields = [
                FieldSchema(name="docID", dtype=DataType.INT64, is_primary=True),
                FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=vector_dim),
                FieldSchema(name="fileName", dtype=DataType.VARCHAR, max_length=512),
                FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535)
            ]
            schema = CollectionSchema(fields, "Knowledge base vector collection")
            collection = Collection(name=self.__collectionName, schema=schema)
            collection.create_index(
                field_name="embedding",
                index_params={
                    "index_type": "IVF_FLAT",
                    "metric_type": "IP",
                    "params": {"nlist": 128}
                }
            )
            print(f"Collection {self.__collectionName} created.")    

    def docInsert(self, embeddings, fileName, texts, ids):
        collection = Collection(self.__collectionName)
        collection.insert([ids, embeddings, [fileName] * len(embeddings), texts])
        collection.flush()
        st.write(f"Inserted {len(embeddings)} segments from '{fileName}' into {self.__collectionName}.")

    def docDelete():
        return
    
    def query(self, vector, top_k=5):
        collection = Collection(self.__collectionName)
        collection.load()
        search_params = {"metric_type": "IP", "params": {"nprobe": 10}}
        results = collection.search([vector], "embedding", search_params, limit=top_k, output_fields=["docID", "fileName", "text"])
        return results

    def list_all_filenames(self):
        collection = Collection(self.__collectionName)
        collection.load()
        results = collection.query(expr="", output_fields=["fileName"], limit=1000)
        file_names = list(set(result["fileName"] for result in results))

        st.write(f"Unique fileNames stored in collection '{self.__collectionName}':")
        for file_name in file_names:
            st.write(file_name)