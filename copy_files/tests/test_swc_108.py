""" tests for SWC 108 vulnerabilities """
# BYTES GOES ALL THE WAY UP TO 32...

from brownie import accounts, SimpleStorage
import os


def convert_to_words(lst):
    return [i for item in lst for i in item.split()]


def test_SWC_108_1(json_metadata):
    json_metadata["error_message"] = "Missing state variable visibility"
    visibility_keywords = ["public", "internal", "private"]
    variable_keywords = [
        "bool",
        "address",
        "byte",
        "bytes1",
        "bytes2",
        "bytes3",
        "int",
        "uint",
    ]

    CONTRACT_NAME = os.listdir("./contracts")[0]
    open_brackets = 0

    with open(f"/contracts/{CONTRACT_NAME}", "r") as f:
        for line in f.readlines():

            # monitor if parsing is inside a function
            if "{" in line):
                open_brackets += 1
            if "}" in line:
                open_brackets -= 1

            # if outside function check for visibility keyword on variables
            if open_brackets == 1:
                words = convert_to_words(line.strip())
                if words[0] in variable_keywords:
                    assert words[1] in visibility_keywords
