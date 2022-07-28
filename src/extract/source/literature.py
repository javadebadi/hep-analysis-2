import os
from pyinspirehep import Client
from shared import (
    write_date_to_source_literature,
    SOURCE_LITERATURE_PATH,
    SOURCE_LITERATURE_ARCHIVED_PATH,
    makedirs,
    get_list_of_files_in_directory,
    )
import logging


client = Client()


def get_head_control_number(min_control_number: int) -> int:
    """Returns the maximum contorl number to start getting source data.

    The fucntions finds the maximum control number in downloaded literature
    and compares it with min_control_number. Finally, it will return the
    head control number

    Parameters
    ----------
    min_control_number : int
        The minimum control number to set as head control number
        when no downloaded source file could be found

    Returns
    -------
    head_control_number : int
        The greates control number for which some data is downloaded and 
        stored in files in literature or literature/archived directories.
    """
    files = get_list_of_files_in_directory(SOURCE_LITERATURE_PATH)
    archived_files = get_list_of_files_in_directory(SOURCE_LITERATURE_ARCHIVED_PATH)
    max_files = None
    max_archived = None
    # if there isn't any file in literature and archived directory
    # set the contorl number to min_control_number
    head_control_number = min_control_number
    # find maximum control number of files inside literature directory
    if files:
        max_files = max(
            int(item.split('_')[0])for item in files
            )
        head_control_number = max(max_files, head_control_number)
    # find maximum control number of files inside archived literature directory
    if archived_files:
        max_archived = max(
            int(item.split('_')[0]) for item in archived_files
            )
        head_control_number = max(max_archived, head_control_number)
    print(f"[EXTRACT: SOURCE] head control number = {head_control_number}")
    return head_control_number


# TODO: future: this field: 'references.record' 
def extract_source_literature_by_control_number(
    control_number_start,
    control_number_end,
    size=10,
    ):
    print(f"[EXTRACT:SOURCE] {control_number_start} - {control_number_end} - size = {size}")
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
        head_control_number = get_head_control_number(min_control_number)
        extract_source_literature(
            size=size,
            resume=False,
            min_control_number=head_control_number,
            max_control_number=max_control_number,
            )

