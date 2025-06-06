"""
This code creates a surfer-themed chatbot using LangChain with memory support. 
It uses ChatMessageHistory to store a chat log in RAM and RunnableWithMessageHistory 
to inject/retrieve this history on each interaction. The MessagesPlaceholder ensures 
prior messages are included in the prompt. get_memory always returns the same memory, 
so all turns share a single history. No data is persisted; memory is session-wide and 
cleared on exit.
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

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
        ("system", "{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

memory = ChatMessageHistory()

def get_memory(session_id):
    return memory

chat_chain = prompt | chat_llm | StrOutputParser()

chat_with_message_history = RunnableWithMessageHistory(
    chat_chain,
    get_memory,
    input_messages_key="question",
    history_messages_key="chat_history",
)


current_weather = """
    {
        "surf": [
            {"beach": "Fistral", "conditions": "6ft waves and offshore winds"},
            {"beach": "Bells", "conditions": "Flat and calm"},
            {"beach": "Watergate Bay", "conditions": "3ft waves and onshore winds"}
        ]
    }"""

# chat_with_message_history build with chat_with_message_history = RunnableWithMessageHistory  
while (question := input("> ")) != "exit":

    response = chat_with_message_history.invoke(
        {
            "context": current_weather,
            "question": question,
            
        }, 
        config={
            "configurable": {"session_id": "none"}
        }
    )
    
    print(response)