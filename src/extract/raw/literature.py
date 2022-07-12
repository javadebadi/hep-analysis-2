import os
import json
from shared import (
    SOURCE_LITERATURE_PATH,
    RAW_LITERATURE_PATH,
    write_date_to_raw_literature,
    makedirs,
    )
import logging


def extract_raw_literature(resume=True):
    makedirs()
    raw_files = os.listdir(RAW_LITERATURE_PATH)
    source_files = os.listdir(SOURCE_LITERATURE_PATH)
    print(source_files)
    print(raw_files)
    for file in source_files:
        if file not in raw_files:
            source_file_path = os.path.join(SOURCE_LITERATURE_PATH, file)
            raw_file_path = os.path.join(RAW_LITERATURE_PATH, file)
            with open(source_file_path, 'r') as fp:
                source_data = json.load(fp)
                source_data = source_data['hits']['hits']
                raw_data = []
                for source_item in source_data:
                    metadata = source_item['metadata']
                    d = {}
                    d['title'] = metadata.get('titles', [{"title": None}])[0]["title"]
                    d['control_number'] = metadata['control_number']
                    d['authors_ids'] = []
                    authors = metadata.get("authors", None)
                    if authors:
                        print(authors[0].keys())
                        records = [
                            author.get("record", None) 
                            for author
                            in authors
                        ]
                        print(records)
                        for record in records:
                            if record is not None:
                                d['authors_ids'].append(record['$ref'].split("/")[-1])
                            print(d['authors_ids'])
                    else:
                        d['authors_ids'] = []
                    raw_data.append(d)
                write_date_to_raw_literature(raw_data, file)
