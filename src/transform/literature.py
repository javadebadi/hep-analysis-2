"""
A module to transform extracted raw literature data
to authors, literature and their relations
"""

import os
import json
import pandas as pd

from shared import (
    RAW_LITERATURE_PATH,
    TRANSFORMED_LITERATURE_PATH,
    makedirs,
)

def read_raw_data_literature_file(filename):
    with open(
        os.path.join(RAW_LITERATURE_PATH, filename),
        'r',
        ) as fp:
        data = json.load(fp)
    return data

def transform_raw_data_literature_file(file):
    makedirs()
    authors = set()
    literature = set()
    has_authored = set()
    data = read_raw_data_literature_file(file)
    for item in data:
        literature_control_number = item["control_number"]
        new_authors = item["authors_ids"]
        # example: new_authors = ["65646", "664349"]
        [authors.add(a) for a in new_authors]
        new_literature = (
            literature_control_number,
            item["title"],
            )
        # example: new_literaute = {"control_number": 546, "title": "X is Y"}
        literature.add(new_literature)
        for new_author in new_authors:
            has_authored.add(
                (new_author, literature_control_number, 'has_authored')
            )

    authors = pd.DataFrame({"author_id": list(authors)})
    literature = pd.DataFrame(
        {
            "control_number": [l[0] for l in literature],
            "title": [l[1] for l in literature],
        }
        )
    has_authored = pd.DataFrame(
        {
            "author_id": [l[0] for l in has_authored],
            "control_number": [l[1] for l in has_authored],
            "has_authored": [l[2] for l in has_authored],
        }
        )
    authors.to_json(
        os.path.join(
            TRANSFORMED_LITERATURE_PATH,
            'authors_'+str(file).replace('.json', '.json')
            ),
            orient='records',
            )
    literature.to_json(
        os.path.join(
            TRANSFORMED_LITERATURE_PATH,
            'literature_'+str(file).replace('.json', '.json')
            ),
            orient='records',
            )
    has_authored.to_json(
        os.path.join(
            TRANSFORMED_LITERATURE_PATH,
            'has_authored_'+str(file).replace('.json', '.json')
            ),
            orient='records',
            )

def transform_raw_data_literature():
    files = os.listdir(RAW_LITERATURE_PATH)
    if files:
        for file in files:
            transform_raw_data_literature_file(file)
            

def main():
    transform_raw_data_literature()