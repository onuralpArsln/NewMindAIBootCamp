from neo4j import GraphDatabase
from dotenv import load_dotenv
load_dotenv()  # take environment variables
import os

USERNAME_NEO= os.getenv('USERNAME_NEO')
PASSWORD = os.getenv('PASSWORD')

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://a5d568d8.databases.neo4j.io"
AUTH = (USERNAME_NEO, PASSWORD)

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()