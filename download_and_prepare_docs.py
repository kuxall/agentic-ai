import os
import requests
from bs4 import BeautifulSoup

DOCS = [
    # Langchain
    ("langchain_custom_agent.txt", "https://python.langchain.com/docs/how_to/agents/custom_agent"),
    ("langchain_agent_executor.txt", "https://python.langchain.com/docs/how_to/agents/agent_executor"),
    ("langchain_memory.txt", "https://python.langchain.com/docs/how_to/chatbots/memory"),
    ("langchain_rag.txt", "https://python.langchain.com/docs/how_to/rag"),
    ("langchain_concept_agents.txt", "https://python.langchain.com/docs/concepts/agents"),
    ("langchain_concept_memory.txt", "https://python.langchain.com/docs/concepts/memory"),
    ("langchain_concept_tools.txt", "https://python.langchain.com/docs/concepts/tools"),
    ("langchain_concept_retrieval.txt", "https://python.langchain.com/docs/concepts/retrieval"),
    ("langchain_concept_vectorstores.txt", "https://python.langchain.com/docs/concepts/vectorstores"),
    # LangGraph Guides
    ("langgraph_agent_architectures.txt", "https://langchain-ai.github.io/langgraph/guides/agent-architectures/"),
    ("langgraph_memory.txt", "https://langchain-ai.github.io/langgraph/guides/memory/"),
    ("langgraph_human_in_the_loop.txt", "https://langchain-ai.github.io/langgraph/guides/human-in-the-loop/"),
    ("langgraph_prebuilt_agents.txt", "https://langchain-ai.github.io/langgraph/guides/prebuilt-agents/"),
    ("langgraph_streaming.txt", "https://langchain-ai.github.io/langgraph/guides/streaming/"),
    ("langgraph_persistence.txt", "https://langchain-ai.github.io/langgraph/guides/persistence/"),
]

DOCS_DIR = "docs"
os.makedirs(DOCS_DIR, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}

def clean_text(text):
    return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

def fetch_and_save(url, filename):
    print(f"Fetching {url}")
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    main = soup.find("main") or soup.body
    text = main.get_text(separator="\n") if main else soup.get_text()
    text = clean_text(text)
    with open(os.path.join(DOCS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved {filename}")

def main():
    for filename, url in DOCS:
        try:
            fetch_and_save(url, filename)
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

if __name__ == "__main__":
    main() 