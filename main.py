from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch




  

def main():
    print("Hello from langchain-course!")
    llm=ChatOllama(model="llama3.2", temperature=0)
    tools=[TavilySearch()]
    agent=create_agent(model=llm,tools=tools)
    result=agent.invoke({"messages":[HumanMessage(content="Search for jobs in AI and ML")]})
    print(result)
  


if __name__ == "__main__":
    main()
