"""Configuration of Neo4j database
"""
# Import the neo4j dependency
from neo4j import GraphDatabase

# Create a new Driver instance
DRIVER = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "test")
    )

# verify connection
DRIVER.verify_connectivity()

