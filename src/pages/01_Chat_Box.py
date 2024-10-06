import streamlit as st
from modules.ai import chat, embedding
from modules.prompts import Prompts
from modules.milvusDB import MilvusDB
from css.layout import set_header

set_header("Ask me everything about law.")

vectorDB = MilvusDB()

if 'prompts' not in st.session_state:
    st.session_state['prompts'] = Prompts("You are a legal specialist.")

query = st.text_area("Enter your question:")
if st.button("Ask"):
    query_emb = embedding(query)
    results = vectorDB.query(query_emb)
    if results:
        st.write("Top results:")
        for result in results:
            for hit in result:
                st.write(f"Document ID: {hit.entity.get('docID')}, File Name: {hit.entity.get('fileName')}, Text: {hit.entity.get('text')}")
    else:
        st.write("No relevant documents found.")
    
    # prompt = query
    # st.session_state['prompts'].userPrompt(prompt)
    # response = agent.chat(st.session_state['prompts'].prompts)
    # st.write(response)