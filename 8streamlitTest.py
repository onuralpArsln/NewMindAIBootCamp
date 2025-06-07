from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_community.graphs import Neo4jGraph


# Initialize the Neo4j graph using Streamlit secrets
graph = Neo4jGraph(
    url=st.secrets["NEO4J_URI"],
    username=st.secrets["NEO4J_USERNAME"],
    password=st.secrets["NEO4J_PASSWORD"],
)

# Example query to test
result = graph.query("MATCH (n) RETURN n LIMIT 5")
st.write(result)

#streamlit run 8streimlitTest.py