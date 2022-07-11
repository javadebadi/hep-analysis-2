import os
import json
from ..base import (
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

#     for file in files:


# def extract_raw_literature_by_control_number(
#     control_number_start,
#     control_number_end,
#     size=10,
#     ):
#     for page in range(1, 10000 // size + 1):
#         try:
#             filename = f'{control_number_start}_{control_number_end}_page{page}_size{size}.json'
#             write_date_to_raw_literature(
#                 literaute_data,
#                 f'{control_number_start}_{control_number_end}_page{page}_size{size}.json'
#                 )
#         except Exception as e:
#             logging.error("EXTRACT ERROR: raw data extraction error")
#             logging.error(f'{control_number_start}_{control_number_end}_page{page}_size{size}.json')
#             logging.exception(e)

# def extract_source_literature(
#     size=10,
#     resume=False,
#     min_control_number=1,
#     max_control_number=2000000,
#     ):
#     if resume is False:
#         for control_number in range(min_control_number, max_control_number, 10000):
#             extract_raw_literature_by_control_number(control_number, control_number+9999, size)
#     else:
#         makedirs()
#         files = os.listdir(RAW_LITERATURE_PATH)
#         if files:
#             head_control_number = int(max(
#                 item.split('_')[0] for item
#                 in files
#             ))
#         else:
#             head_control_number = min_control_number
#         extract_source_literature(
#             size=size,
#             resume=False,
#             min_control_number=head_control_number,
#             max_control_number=max_control_number,
#             )
