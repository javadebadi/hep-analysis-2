import os
from .exception import MissingRequiredFieldError
from .schema_primitive import SchemaPrimitive

class SchemaObject:

    def __init__(
        self,
        name=None,
        type_=None,
        properties=None,
        additionalProperties=None,
        title=None,
        required=None,
        ) -> None:
        self.required = required
        self.type_ = type_
        self.properties = properties
        self.additionalProperties = additionalProperties
        self.title = title
        self.name = name
        self.old_new_keys = {}
        self.new_old_keys = {}
        self.clean()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if "_" in name:
            self._name = "".join([n.capitalize() for n in name.split("_")])
        else:
            self._name = name[0].capitalize() + name[1:]

    def _clean_property_key(self, property_key):
        if property_key == '$schema':
            property_key = 'schema'
        elif property_key == 'self':
            property_key = 'self_'
        elif property_key.startswith("_"):
            property_key = property_key[1:]
        else:
            property_key = property_key
        return property_key

    def keys(self):
        return self.properties.keys()

    def values(self):
        return self.properties.values()

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        for key in self.required:
            if not key in properties.keys():
                raise MissingRequiredFieldError(
                    f"required key = '{key}' is missing"
                )
        self._properties = properties

    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, required=None):
        if required is None:
            self._required = []
        else:
            assert type(required) == list
            self._required = required

    def clean(self):
        keys_to_drop = set()
        d = {}
        if self.properties is not None:
            for property_key, property_value in self.properties.items():
                new_key = self._clean_property_key(property_key)
                d[new_key] = property_value
                if new_key != property_key:
                    keys_to_drop.add(property_key)
                self.old_new_keys.update({property_key: new_key})
                self.new_old_keys.update({new_key: property_key})
            for key in keys_to_drop:
                del self.properties[key]
            self.properties.update(d)

    def get_annotation_type(
        self,
        force_dict=False,
        colons=True,
        ):
        annotation_type = ''
        if self.name is None:
            if force_dict is True:
                annotation_type += 'dict'
            else:
                annotation_type += 'object'
        else:
            annotation_type += self.name
        return ": " + annotation_type if colons else annotation_type

    def get_python_type(self, force_dict=False):
        python_type = ''
        if self.name is None:
            if force_dict is True:
                python_type += 'dict'
            else:
                python_type += 'object'
        else:
            python_type += self.name
        return python_type

    def get_default_value(self):
        return " = None"

    def set_from_dict(self, schema_data):
        return SchemaObject(
            name=self.name,
            required=schema_data.get('required', []),
            type_=schema_data['type'],
            additionalProperties=schema_data.get('additionalProperties', None),
            properties=schema_data.get('properties', None),
            title=schema_data.get('title', None),
        )

    def _get_class_name(self):
        if self.name is not None:
            return self.name
        else:
            return "".join([token.capitalize() for token in self.title.split(" ")])

    def _build_properties_data_type(self):
        self.processed_properties = {}
        data_types_code = ''
        for property_key, property_value in self.properties.items():
            if property_value['type'] == 'object':
                self.processed_properties[property_key] = SchemaObject(property_key).set_from_dict(property_value)
                data_types_code += self.processed_properties[property_key].get_python_class() + "\n\n"
            elif property_value['type'] in ['string', 'int', 'boolean']:
                x = SchemaPrimitive(property_key).set_from_dict(property_value)
                self.processed_properties[x.name] = x
                self.old_new_keys.update(x.name_mapping)
        return data_types_code

    def get_python_class(self, imports_part=False):
        data_types_code = self._build_properties_data_type()
        if imports_part:
            s = "import typing\n\n\n" # import line
        else:
            s = ""
        s += data_types_code
        s += f"class {self._get_class_name()}:\n\n" # define class
        # < __init__ 
        s += "\tdef __init__(\n"
        s += "\t"*2 + "self," + "\n"
        if len(self.processed_properties) > 0:
            for key, schema_object in self.processed_properties.items():
                # init def and args
                s += "\t"*2 + key + schema_object.get_annotation_type() + " " + schema_object.get_default_value() + ",\n"
        s += "\t"*2 + ") -> None:" + "\n"
        # init body
        if len(self.processed_properties) > 0:
            for key, schema_object in self.processed_properties.items():
                s += "\t"*2 + f"self.{key} = {key}\n"
        else:
            s += "\t"*2 + "pass\n"
        # __init__ />
        s += "\n"

        # @property
        if len(self.processed_properties) > 0:
            for key, schema_object in self.processed_properties.items():
                if type(schema_object) == SchemaPrimitive:
                    s += schema_object.get_as_property_in_class_code()
                elif type(schema_object) == SchemaObject:
                    s += schema_object.get_as_property_in_class_code(property_key=key)
        return s

    def write_python_class(self, base_path=None):
        s = self.get_python_class(imports_part=True)
        if self.name is None:
            filepath = "model.py"
        else:
            filepath = self.name.lower() + ".py"
        if base_path is not None:
            os.makedirs(base_path, exist_ok=True)
            filepath = os.path.join(base_path, filepath)
        with open(filepath, "w") as f:
            f.write(s)
        return s

    def get_as_property_in_class_code(self, tabs=1, property_key=None):
        if property_key is None:
            name = self.name
        else:
            name = property_key
        s = "\t"*tabs + "@property\n"
        s += "\t"*(tabs) + f"def {name}(self) -> " + self.get_annotation_type(colons=False) + ":\n"
        s += "\t"*(tabs + 1) + f"return self.{name}\n"
        s += "\n"
        return s
