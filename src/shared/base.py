import os
import shutil
import json

DATA_PATH = os.path.join('data')
SOURCE_PATH = os.path.join(DATA_PATH, 'source')
RAW_PATH = os.path.join(DATA_PATH, 'raw')
TRANSFORMED_PATH = os.path.join(DATA_PATH, 'transformed')
SOURCE_LITERATURE_PATH = os.path.join(SOURCE_PATH, 'literature')
SOURCE_LITERATURE_ARCHIVED_PATH = os.path.join(SOURCE_LITERATURE_PATH, 'archived')
RAW_LITERATURE_PATH = os.path.join(RAW_PATH, 'literature')
RAW_LITERATURE_ARCHIVED_PATH = os.path.join(RAW_LITERATURE_PATH, 'archived')
TRANSFORMED_LITERATURE_PATH = os.path.join(TRANSFORMED_PATH, 'literature')
TRANSFORMED_LITERATURE_ARCHIVED_PATH = os.path.join(TRANSFORMED_LITERATURE_PATH, 'archived')

def makedirs():
    os.makedirs(SOURCE_PATH, exist_ok=True)
    os.makedirs(RAW_PATH, exist_ok=True)
    os.makedirs(TRANSFORMED_PATH, exist_ok=True)
    os.makedirs(SOURCE_LITERATURE_PATH, exist_ok=True)
    os.makedirs(RAW_LITERATURE_PATH, exist_ok=True)
    os.makedirs(TRANSFORMED_LITERATURE_PATH, exist_ok=True)
    os.makedirs(SOURCE_LITERATURE_ARCHIVED_PATH, exist_ok=True)
    os.makedirs(RAW_LITERATURE_ARCHIVED_PATH, exist_ok=True)
    os.makedirs(TRANSFORMED_LITERATURE_ARCHIVED_PATH, exist_ok=True)

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

def write_data_to_raw(obj, filename, subdirectory_name):
    """Writes given json data to raw directory
    """
    makedirs()
    with open(
        os.path.join(
            os.path.join(RAW_PATH, subdirectory_name),
            filename),
            'w'
            ) as fp:
        json.dump(obj, fp, sort_keys=True, indent=4)

def write_date_to_raw_literature(obj, filename):
    write_data_to_raw(obj, filename, 'literature')

def archive_source_literature_file(filename):
    shutil.move(
        os.path.join(SOURCE_LITERATURE_PATH, filename),
        os.path.join(SOURCE_LITERATURE_ARCHIVED_PATH, filename),
        )