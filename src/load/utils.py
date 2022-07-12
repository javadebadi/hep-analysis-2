import logging
from neo4j.exceptions import ClientError
from .settings import DRIVER

def create_node_index(node, field):
    try:
        createIndex = f"CREATE INDEX ON :{node}({field})"
        with DRIVER.session() as session:
            session.run(createIndex)
    except ClientError as e:
        logging.error(e)


def create_relationship_index(relationship, field):
    try:
        createIndex = f"""CREATE INDEX {relationship}_{field}
        FOR ()-[r:{relationship}]-()
        ON (r.{field});
        """
        with DRIVER.session() as session:
            session.run(createIndex)
    except ClientError as e:
        logging.error(e)