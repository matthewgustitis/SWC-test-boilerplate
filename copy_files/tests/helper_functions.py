import importlib
import os

# remove empty lines and trailing whitespace from file
def remove_whitespace(file):
    lines = file.readlines()
    lines = [s.strip() for s in lines]
    return [s for s in lines if s]


# get ContractContainer of main contract
def get_contract():
    CONTRACT_NAME = os.listdir("./contracts")[0]
    CONTRACT_NAME = CONTRACT_NAME.split(".")[0]
    return getattr(importlib.import_module("brownie"), CONTRACT_NAME)


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
