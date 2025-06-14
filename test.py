from typing import List
from fastapi import FastAPI
from langchain.llms import Ollama
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langserve import add_routes
import uvicorn
import markdown

llm = Ollama(model="qwen3:1.7b")
template = PromptTemplate.from_template("create a project on {topic}.")
chain = template | llm 
# | markdown.markdown

app = FastAPI(title="LangChain", version="1.0", description="The first server ever!")
add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)