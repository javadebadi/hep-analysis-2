import json
import os
from charset_normalizer import logging
import pandas as pd
from shared import (
    TRANSFORMED_LITERATURE_PATH,
    archive_transformed_literature_file,
    get_list_of_files_in_directory,
)
import logging
from .utils import create_node_index
from .settings import DRIVER

def read_transfomred_file(file, prefix):
    if str(file).startswith(prefix):
        with open(
            os.path.join(
                TRANSFORMED_LITERATURE_PATH,
                file
            ),
            'r',
        ) as f:
            data_list = json.load(f)
        return data_list
    else:
        return None

# Authors

def read_transformed_authors(file):
    return read_transfomred_file(file, 'authors_')

def read_transfomred_literature(file):
    return read_transfomred_file(file, 'literature_')

def read_transfomred_has_authored(file):
    return read_transfomred_file(file, 'has_authored_')


def load_authors_from_file(file):
    data_list = read_transformed_authors(file)
    if not data_list:
        return None
    lines = []
    for number, item in enumerate(data_list):
        line = "MERGE (a" + str(number) + ":Author {author_id:'"
        line += item["author_id"] + "'})"
        if item["title"]:
            line += 'SET a' +  str(number) + '.title = "' +  r"{}".format(item["title"]).replace("\n","").replace("\"","'") +  '"'
        else:
            line += 'SET a' +  str(number) + '.title = NULL'
        lines.append(line)
    
    with DRIVER.session() as session:
        for line in lines:
            cquery = line
            results = session.run(cquery)
    # archive the transformed file after done with it
    archive_transformed_literature_file(file)

def load_literature_from_file(file):
    data_list = read_transfomred_literature(file)
    if not data_list:
        return None
    lines = []
    for number, item in enumerate(data_list):
        s = "MERGE (a" + str(number) + ":Literature {control_number:"
        s += str(item["control_number"]) + "})\n"
        if item["control_number"]:
            s += 'SET a' +  str(number) + '.title = "' +  r"{}".format(item["title"]).replace("\n","").replace("\"","'") +  '"'
            # clean the unicode character
            s = s.replace(r"\u", "BACKSLASHu")
        else:
            s += 'SET a' +  str(number) + '.title = NULL'
        if s.strip() != "":
            lines.append(s)

    with DRIVER.session() as session:
        for cqeury in lines:
            print("<<<--------------------------")
            results = session.run(cqeury)
            print("-------------------------->>>>")

    # archive the transformed file after done with it
    archive_transformed_literature_file(file)

def load_has_authored_from_file(file):
    data_list = read_transfomred_has_authored(file)
    if not data_list:
        return None
    lines = []
    for number, item in enumerate(data_list):
        # line 1: match author query 
        s = "MATCH (a" + str(number) + ":Author {author_id:'"
        s += str(item["author_id"]) + "'})\n"
        # line 2: match literature query 
        s += "MATCH (l" + str(number) + ":Literature {control_number: "
        s += str(item["control_number"]) + "})\n"
        # line 3: merge relationship
        s += f"MERGE (a{number})-[:HAS_AUTHORED]->(l{number})\n"
        lines.append(s)

    with DRIVER.session() as session:
        for cqeury in lines:
            print("<<<             -[]->")
            print(cqeury)
            results = session.run(cqeury)
            print("-[]->             >>>>")

    # archive the transformed file after done with it
    archive_transformed_literature_file(file)

    
def load_authors():
    # create index on a node
    node = 'Author'  # Label of the node
    create_node_index(node, 'author_id')

    for file in get_list_of_files_in_directory(TRANSFORMED_LITERATURE_PATH):
        load_authors_from_file(
            file,
            )
    
def load_literature():
    # create index on a node
    node = 'Literature'  # Label of the node
    create_node_index(node, 'control_number')

    for file in get_list_of_files_in_directory(TRANSFORMED_LITERATURE_PATH):
        load_literature_from_file(file)
    
def load_has_authored():
    # create index on a node
    node = 'Literature'  # Label of the node
    create_node_index(node, 'control_number')

    for file in get_list_of_files_in_directory(TRANSFORMED_LITERATURE_PATH):
        load_has_authored_from_file(file)