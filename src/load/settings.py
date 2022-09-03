"""Configuration of Neo4j database
"""
# Import the neo4j dependency
from neo4j import GraphDatabase

# Create a new Driver instance
USERNAME = "neo4j"
PASSWORD = "test"
URI = "bolt://localhost:7687"

DRIVER = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
    )

# verify connection
DRIVER.verify_connectivity()

