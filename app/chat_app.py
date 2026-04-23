import streamlit as st
from rag_pipeline import get_qa_chain
from loader import load_pdf
from embeddings import get_embeddings
from vector_store import create_vector_store

st.title("Multi-Document RAG Chatbot")

uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files:
    docs = []

    for file in uploaded_files:
        docs.extend(load_pdf(file))   # ✅ returns Document objects

    embeddings = get_embeddings()
    vectorstore = create_vector_store(docs, embeddings)

    qa_chain = get_qa_chain(vectorstore)

    query = st.text_input("Ask a question")

    if query:
        response = qa_chain.run(query)
        st.write(response)