import os
import json

DATA_PATH = os.path.join('data')
SOURCE_PATH = os.path.join(DATA_PATH, 'source')
RAW_PATH = os.path.join(DATA_PATH, 'raw')
SOURCE_LITERATURE_PATH = os.path.join(SOURCE_PATH, 'literature')
RAW_LITERATURE_PATH = os.path.join(RAW_PATH, 'literature')

def makedirs():
    os.makedirs(SOURCE_PATH, exist_ok=True)
    os.makedirs(RAW_PATH, exist_ok=True)
    os.makedirs(SOURCE_LITERATURE_PATH, exist_ok=True)
    os.makedirs(RAW_LITERATURE_PATH, exist_ok=True)

def write_data_to_source(obj, filename, subdirectory_name):
    """Writes given json data to source directory
    """
    makedirs()
    with open(
        os.path.join(
            os.path.join(SOURCE_PATH, subdirectory_name),
            filename),
            'w'
            ) as fp:
        json.dump(obj, fp, sort_keys=True, indent=4)

def write_date_to_source_literature(obj, filename):
    write_data_to_source(obj, filename, 'literature')