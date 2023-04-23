from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.tools import BaseTool
import os

load_dotenv()

def extract_passages(file_path):
    # Open file and read contents
    with open(file_path, 'r') as file:
        contents = file.read()

    # Split contents into passages
    passages = contents.split('---')

    # Strip whitespace from each passage and remove empty passages
    passages = [p.strip() for p in passages if p.strip()]

    # Return array of passages
    return passages

def extract_longtext(file_path):
    # Open file and read contents
    with open(file_path, 'r') as file:
        contents = file.read()

    string_batches = [contents[i:i+1000] for i in range(0, len(contents), 1000)]

    # Return array of passages
    return string_batches

if __name__ == '__main__':
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    #knowledge_text_strings = extract_passages("knowledge.txt")
    knowledge_text_strings = extract_longtext("knowledge_food.txt")
    print(knowledge_text_strings)
    doc_store = Qdrant.from_texts(knowledge_text_strings, embeddings)
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    #qa = RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",vectorstore=doc_store,return_source_documents=False)
    qa = RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=doc_store.as_retriever())

    tools_corporate = [
        Tool(
            name = "Get some info from knowledge base",
            func=qa.run,
            description="useful for when you need to answer questions about the investment fund administration. Input should be a fully formed question."
        )
    ]
    tools_food_knowledge = [
        Tool(
            name = "Get some info about the US Food and Drug Administration (FDA)",
            func=qa.run,
            description="useful for when you need to answer questions about the US Food and Drug Administration (FDA). Input should be a fully formed question."
        )
    ]

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    #question = "muss ich ein Abschluss nach HGB machen wenn ich einen Investmentfonds betreibe?"
    question = "Make a short instagram post text about applied nutrition approved by the FDA"
    print (question)
    print(agent.run(question))








