import os
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from glob import glob
import streamlit as st

load_dotenv()

# Config
DATA_PATH = "docs"
VECTOR_STORE_PATH = "faiss_index"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

os.makedirs(DATA_PATH, exist_ok=True)

def ingest_documents():
    """Load, chunk, embed, and store documents in FAISS."""
    filepaths = glob(os.path.join(DATA_PATH, "*.txt"))
    docs = []
    for filepath in filepaths:
        loader = TextLoader(filepath, encoding="utf-8")
        docs.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    splits = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(splits, embeddings)
    vectorstore.save_local(VECTOR_STORE_PATH)
    return vectorstore

def load_vectorstore():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)

def build_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are a helpful assistant. Use the following context to answer the question.
    Context: {context}
    Question: {question}
    Answer:
    """
    )
    llm = OpenAI(temperature=0)
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )

def get_chain():
    if not os.path.exists(VECTOR_STORE_PATH):
        vectorstore = ingest_documents()
    else:
        vectorstore = load_vectorstore()
    return build_qa_chain(vectorstore)

st.set_page_config(page_title="LangChain/LangGraph RAG Assistant", layout="wide")
st.title("LangChain & LangGraph Technical Assistant")

if "qa_chain" not in st.session_state:
    st.session_state["qa_chain"] = get_chain()

question = st.text_input("Ask a developer question about LangChain or LangGraph:")

if question:
    with st.spinner("Retrieving answer..."):
        result = st.session_state["qa_chain"].invoke({"query": question})
        answer = result["result"]
        st.markdown(f"**Answer:** {answer}")
        sources = result.get("source_documents", [])
        if sources:
            st.markdown("**Sources:**")
            for doc in sources:
                st.markdown(f"- {doc.metadata.get('source', 'unknown')}")

