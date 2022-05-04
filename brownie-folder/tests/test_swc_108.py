""" tests for SWC 108 vulnerabilities (State Variable Default Visibility) """
# BYTES GOES ALL THE WAY UP TO 32...

from brownie import accounts, SimpleStorage
from helper_functions import remove_whitespace
import os


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
    in_contract = False
    open_brackets = 0

    with open(f"contracts/{CONTRACT_NAME}", "r") as f:
        lines = remove_whitespace(f)

        for line in lines:
            words = line.split()
            print(words)
            assert False

            if words[0] == "contract":
                in_contract = True
                open_brackets = 1

            # when open_brackets is 1, check for variables. when it's 0, in_contract = false
            if in_contract:
                if "{" in words[-1]:
                    open_brackets += 1
                if "}" in words[-1]:
                    open_brackets -= 1

                # finish test when out of contract
                if open_brackets == 0:
                    break

                # check for visibility keywords for state variables
                if open_brackets == 1:
                    if words[0] in variable_keywords:
                        assert words[1] in visibility_keywords
