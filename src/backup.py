"""A module to backup neo4j database (loaded database)
"""

from load.settings import DRIVER
from shared.base import BACKUP_PATH, makedirs
import os

makedirs()

SEPARATOR = '\t|\t'

with DRIVER.session() as session:
    cquery = f"""
    MATCH (n:Author)
    RETURN n.author_id AS author_id,
           n.title as author_title
    """
    results = session.run(cquery)
    with open(os.path.join(BACKUP_PATH, 'authors.csv'), 'w', encoding='utf-8') as f:
        counter = 0
        for row in results:
            counter += 1
            if counter % 1000 == 0:
                print(counter, " ...")
            f.write(tuple(row)[0] + SEPARATOR + tuple(row)[1])
            f.write('\n')

with DRIVER.session() as session:
    cquery = f"""
    MATCH (n:Literature)
    RETURN n.control_number AS control_number,
           n.title as literature_title
    """
    results = session.run(cquery)
    with open(os.path.join(BACKUP_PATH, 'literature.csv'), 'w', encoding='utf-8') as f:
        counter = 0
        for row in results:
            counter += 1
            if counter % 1000 == 0:
                print(counter, " ...")
            f.write(str(tuple(row)[0]) + SEPARATOR + tuple(row)[1])
            f.write('\n')

with DRIVER.session() as session:
    cquery = f"""
    MATCH (n:Author)-[a:HAS_AUTHORED]->(l:Literature)
    RETURN n.author_id AS author_id,
            n.title AS author_title,
            l.title AS literature_title,
            l.control_number AS control_number
    """
    results = session.run(cquery)
    with open(os.path.join(BACKUP_PATH, 'has_authored.csv'), 'w', encoding='utf-8') as f:
        counter = 0
        for row in results:
            counter += 1
            if counter % 1000 == 0:
                print(counter, " ...")
            s = tuple(str(x) for x in tuple(row))
            f.write(s[0] + SEPARATOR + s[1] + SEPARATOR)
            f.write(s[2] + SEPARATOR + s[3])
            f.write('\n')

