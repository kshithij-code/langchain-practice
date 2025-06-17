from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from test_agent import *

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
    # reply_stream=agent.stream({"messages": [SystemMessage(content="reply in markdown that can be converted into html"),
    #                                  HumanMessage(content=message)]},
    #                                  config={"recursion_limit":100})
         
    messages = reply.get("messages")

    if not messages:
        return {"message": "No response from agent."}
    
    print(messages[-1].content)
    return {"message":str(messages[-1].content)}
