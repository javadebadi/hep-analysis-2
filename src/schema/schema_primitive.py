import os


class SchemaPrimitive:

    def __init__(
        self,
        name=None,
        type_=None,
        enum=None,
        ) -> None:
        self.name_mapping = {}
        self.type_ = type_
        self.name = name
        self.enum = enum

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name.startswith("$"):
            new_name = name[1:]
            self.name_mapping[name] = new_name
        else:
            new_name = name
        self._name = new_name

    def set_from_dict(self, schema_data):
        return SchemaPrimitive(
            name=self.name,
            type_=schema_data["type"],
            )

    def get_annotation_type(
        self,
        force_dict=False,
        colons=True,
        ):
        if self.type_ == 'string':
            return ": str" if colons else "str"
        if self.type_ == 'integer':
            return ": int" if colons else "int"
        if self.type_ == 'boolean':
            return ": bool" if colons else "bool"

    def get_default_value(self):
        return " = None"

    def get_as_property_in_class_code(self, tabs=1, property_key=None):
        s = "\t"*tabs + "@property\n"
        s += "\t"*(tabs) + f"def {self.name}(self) -> " + self.get_annotation_type(colons=False) + ":\n"
        s += "\t"*(tabs + 1) + f"return self.{self.name}\n"
        s += "\n"
        return s

    def get_assertion_expression(self):
        s = ""
        if self.enum:
            s += f"assert self.{self.name} in {self.enum}"
        return s