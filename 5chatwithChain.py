"""
    Chat models are designed to have conversations
    they accept a list of messages and return a conversational response.
"""
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage  
from langchain.schema import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat_llm = ChatOpenAI(
    openai_api_key=os.getenv("AI_KEY"),
      model_name="gpt-4.1-nano" 
    )

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a surfer dude, having a conversation about the surf conditions on the beach. Respond using surfer slang.",
        ),
        (
            "human", 
            "{question}"
        ),
    ]
)

chat_chain = prompt | chat_llm | StrOutputParser()

response = chat_chain.invoke({"question": "What is the weather like?"})

print(response)