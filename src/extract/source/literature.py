import os
from pyinspirehep import Client
from shared import (
    write_date_to_source_literature,
    SOURCE_LITERATURE_PATH,
    makedirs,
    )
import logging

client = Client()

# TODO: future: this field: 'references.record' 
def extract_source_literature_by_control_number(
    control_number_start,
    control_number_end,
    size=10,
    ):
    for page in range(1, 10000 // size + 1):
        try:
            literaute_data = client.search_literature(
                    'authors.record','authors.full_name','titles',
                    sorting='mostrecent',
                    size=size,
                    page=page,
                    q=f'control_number:{control_number_start}->{control_number_end}'
                    )
            write_date_to_source_literature(
                literaute_data,
                f'{control_number_start}_{control_number_end}_page{page}_size{size}.json'
                )
        except Exception as e:
            logging.error("EXTRACT ERROR: source data download error")
            logging.error(f'{control_number_start}_{control_number_end}_page{page}_size{size}.json')
            logging.exception(e)

def extract_source_literature(
    size=10,
    resume=False,
    min_control_number=1,
    max_control_number=2000000,
    ):
    if resume is False:
        for control_number in range(min_control_number, max_control_number, 10000):
            extract_source_literature_by_control_number(control_number, control_number+9999, size)
    else:
        makedirs()
        files = os.listdir(SOURCE_LITERATURE_PATH)
        if files:
            head_control_number = int(max(
                item.split('_')[0] for item
                in files
            ))
        else:
            head_control_number = min_control_number
        extract_source_literature(
            size=size,
            resume=False,
            min_control_number=head_control_number,
            max_control_number=max_control_number,
            )
