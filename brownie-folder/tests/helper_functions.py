# remove empty lines and trailing whitespace from file
def remove_whitespace(file):
    lines = file.readlines()
    lines = [s.strip() for s in lines]
    return [s for s in lines if s]


# all visibility keywords
visibility_keywords = ["public", "internal", "private"]

# all variable keywords
variable_keywords = [
    "bool",
    "string",
    "address",
    "enum",
    "mapping",
    "struct",
    "fixed",
    "ufixed",
    "byte",
    "uint",
    "int",
]
