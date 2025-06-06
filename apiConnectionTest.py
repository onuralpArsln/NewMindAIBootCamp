from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("AI_KEY"),
    model_name="gpt-4.1-nano" 
)

def basicQuesiton():
    response = llm.invoke("What is Neo4j?")
    print(response.content)


from langchain.prompts import PromptTemplate#

template = PromptTemplate(template="""
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Tell me about the following fruit: {fruit}
""", input_variables=["fruit"])

def templateWork():
    response = llm.invoke(template.format(fruit="apple"))
    print(response)

templateWork()