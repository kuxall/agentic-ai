# LangChain & LangGraph RAG Technical Assistant

A Retrieval-Augmented Generation (RAG) assistant that answers developer questions using content from the LangChain and LangGraph documentation. Powered by LangChain, OpenAI, FAISS, and Streamlit.

---

## Features
- **Document Ingestion:** Downloads and chunks focused LangChain/LangGraph docs for retrieval.
- **Vector Store:** Uses FAISS for fast semantic search.
- **LLM-Powered Answers:** Uses OpenAI LLMs to answer questions based on retrieved context.
- **Web UI:** Clean, interactive Streamlit interface.
- **Source Attribution:** Shows which doc(s) answers are based on.

---

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/kuxall/agentic-ai
cd agentic-ai
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Set your OpenAI API key
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your-openai-api-key-here
```

### 4. Download and prepare documentation
This will fetch and clean focused LangChain/LangGraph docs for ingestion:
```
python download_and_prepare_docs.py
```

### 5. Run the Streamlit app
```
streamlit run rag_assistant.py
```

Open the local URL provided by Streamlit in your browser.

---

## Usage
- Enter a developer question about LangChain or LangGraph in the input box.
- The assistant retrieves relevant doc chunks and generates an answer.
- Sources for the answer are shown below the response.

### Example Inputs & Outputs

**Q:** What is a vector store in LangChain and how is it used?

**A:**
> A vector store in LangChain is a specialized data store that enables indexing and retrieving information based on vector representations. It is used to store and query complex relationships between data points, such as social networks, supply-chain management, fraud detection, and recommendation services. It provides a standard interface for working with vector stores, allowing users to easily switch between different vectorstore implementations. The key methods for working with vector stores are add_documents, delete, and similarity_search.

**Sources:**
- docs\langchain_concept_vectorstores.txt
- docs\langchain_concept_vectorstores.txt
- docs\langchain_concept_vectorstores.txt
- docs\langchain_concept_retrieval.txt

---
## Technologies Used
- **LangChain**: For building the RAG pipeline.
- **OpenAI**: For LLM-based question answering.
- **FAISS**: For efficient vector similarity search.
- **Streamlit**: For the web interface.
- **Python**: Core programming language.
- **dotenv**: For environment variable management.
- **Requests**: For downloading documentation files.
- **BeautifulSoup**: For HTML parsing and cleaning.

## Customization
- Add more `.txt` files to the `docs/` folder to expand the knowledge base.
- Adjust chunk size or overlap in `rag_assistant.py` for different retrieval granularity.

## License
MIT 