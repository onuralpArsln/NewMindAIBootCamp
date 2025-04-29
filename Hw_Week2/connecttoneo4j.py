from neo4j import GraphDatabase
from dotenv import load_dotenv
load_dotenv()  # take environment variables

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://f750ff4b.databases.neo4j.io"
AUTH = ("<Username>", "<Password>")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()