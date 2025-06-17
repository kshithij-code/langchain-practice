from datetime import datetime
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from markdown import markdown
from typing import List,Dict,Any
from langchain_core.runnables.base import RunnableLike
from IPython.display import Image
from langchain_tavily import TavilySearch
import getpass
import os
from dotenv import load_dotenv

load_dotenv(".env")

@tool
def solve_expression(expression:str)->str:
    '''return a value after evalutating a python expression using the "eval()" function'''
    return eval(expression)
@tool
def get_date()->datetime:
    '''return today's date'''
    return datetime.now()

@tool
def get_info()->List[str]:
    '''return today's news'''
    return ["Over 80 Killed In Iran, Israel As Missiles Pound Middle East",
            "PM Modi on key 3-nation tour: Cyprus, Canada, Croatia on itinerary; what's on his agenda?",
            "7 killed in helicopter crash in Uttarakhand, chopper services shut"]

if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("Tavily API key:\n")


model = ChatOllama(model="qwen3:1.7b")
tavily_search_tool = TavilySearch(
    max_results=5,
    topic="general",
)
tools = [solve_expression,get_date,get_info]
agent = create_react_agent(model, tools)

if __name__=="__main__":
        reply:Dict[str,List]=agent.invoke({"messages": [HumanMessage(content=input("message:"))]},
                                     config={"recursion_limit":100})
        print(reply["messages"][-1].content)