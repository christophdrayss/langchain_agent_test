# Langchain Agent Test

Simple AI agent that acts as a personal assistant, can research from a knowledge base and over time gets more skills (google search, webscraping, etc.).
The assistant will use a manual, that is enriched time over time.

## Install

1. Create .env file and save OPENAI API KEY: "OPENAI_API_KEY = sk-XXXX"
2. Start docker and run the vector indexer ```docker run -p 6333:6333 qdrant/qdrant```
3. Write some asks in the main.py
4. run ```python main.py```

## Readings 

- Learn about vector indexer: https://qdrant.tech/documentation/  
- Make thoughts chain: https://github.com/hwchase17/langchain/blob/master/docs/getting_started/getting_started.md  
- Setup vectorebase as an agent tool: https://python.langchain.com/en/latest/modules/agents/agent_executors/examples/agent_vectorstore.html