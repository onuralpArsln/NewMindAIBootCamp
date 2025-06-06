import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(
    openai_api_key=os.getenv("AI_KEY"),
      model_name="gpt-4.1-nano" 
    )

template = PromptTemplate.from_template("""
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Output JSON as {{"description": "your response here"}}

Tell me about the following fruit: {fruit}
""")

llm_chain = template | llm | StrOutputParser()
# Adding a StrOutputParser to the chain would ensure a string.


response = llm_chain.invoke({"fruit": "apple"})

print(response)