from fastapi import FastAPI
from datetime import datetime
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from markdown import markdown
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict,List

@tool
def solve_expression(expression:str)->str:
    '''return a value after evalutating a python expression using the "eval()" function'''
    return eval(expression)
@tool
def get_date():
    '''return today's date'''
    return datetime.now()

@tool
def get_info()->list[str]:
    '''return today's news'''
    return ["Over 80 Killed In Iran, Israel As Missiles Pound Middle East",
            "PM Modi on key 3-nation tour: Cyprus, Canada, Croatia on itinerary; what's on his agenda?",
            "7 killed in helicopter crash in Uttarakhand, chopper services shut"]

model = ChatOllama(model="qwen3:1.7b")
tools = [solve_expression,get_date,get_info]
agent = create_react_agent(model, tools)

app=FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root(message:str):
    print(message)
    reply:Dict[str,List] =agent.invoke({"messages": [SystemMessage(content="reply in markdown that can be converted into html"),
                                     HumanMessage(content=message)]},
                                       config={"recursion_limit":100})
    
    messages = reply.get("messages")

    if not messages:
        return {"message": "No response from agent."}
    
    print(messages[-1].content)
    return {"message":str(messages[-1].content)}
