import json
import os
from src.schema import SchemaObject


BASE_PATH = os.path.join(".", "data", "schema")
for filename in os.listdir(BASE_PATH):
    filepath = os.path.join(BASE_PATH, filename)
    name = filename.split(".json")[0]

    with open(filepath, "r") as f:
        schema_data = json.load(f)

    schema_object = SchemaObject(name).set_from_dict(schema_data)
    schema_object.write_python_class("generated_codes")

# print(schema_object.keys())
# print(schema_object.values())

from generated_codes.authors import Authors
AUTHORS_PATH = os.path.join(".", "data", "single", "authors")
with open(os.path.join(AUTHORS_PATH, "1679997.json"), "r") as f:
    data = json.load(f)
a = Authors()
a = a.set_from_dict(data["metadata"])
print(a.name.preferred_name)
print(a)

from generated_codes.institution import Institution
INSTITUTIONS_PATH = os.path.join(".", "data", "single", "institutions")
with open(os.path.join(INSTITUTIONS_PATH, "909187.json"), "r") as f:
    data = json.load(f)
a = Institution()
a = a.set_from_dict(data["metadata"])
print(a)


# print(a.new_record)
# print(data["metadata"])
# print(a.legacy_creation_date)

