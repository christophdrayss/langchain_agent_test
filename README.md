# Langchain Agent Test

Simple AI agent that acts as a personal assistant, can research from a knowledge base and over time gets more skills (google search, webscraping, etc.).
The assistant will use a manual, that is enriched time over time.

## Install

1. Start docker and run the vector indexer ```docker run -p 6333:6333 qdrant/qdrant```
2. Write some asks in the main.py
3. run ```python main.py```

## Readings 

Make thoughts chain: https://github.com/hwchase17/langchain/blob/master/docs/getting_started/getting_started.md
Make vectorebase as an agent tool: https://python.langchain.com/en/latest/modules/agents/agent_executors/examples/agent_vectorstore.html