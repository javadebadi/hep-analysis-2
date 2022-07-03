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
