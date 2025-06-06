"""
    Chat models are designed to have conversations
    they accept a list of messages and return a conversational response.
"""
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage  
from dotenv import load_dotenv

load_dotenv()

chat_llm = ChatOpenAI(
    openai_api_key=os.getenv("AI_KEY"),
      model_name="gpt-4.1-nano" 
    )

instructions = SystemMessage(content="""
You are a surfer dude, having a conversation about the surf conditions on the beach.
Respond using surfer slang.
""")

question = HumanMessage(content="What is the weather like?")



response = chat_llm.invoke([
    instructions,
    question
])

print(response.content)