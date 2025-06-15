from fastapi import FastAPI
from datetime import datetime
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from markdown import markdown
from fastapi.middleware.cors import CORSMiddleware
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
    '''return todays news'''
    return ["Over 80 Killed In Iran, Israel As Missiles Pound Middle East: 10 Points",
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
    reply=agent.invoke({"messages": [HumanMessage(content=message)]})
    print(reply.get("messages")[1].content+" "+reply.get("messages")[-1].content)
    return {"message":markdown(reply.get("messages")[-1].content)}
