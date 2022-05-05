""" tests for SWC 108 vulnerabilities (State Variable Default Visibility) """

from helper_functions import (
    remove_whitespace,
    visibility_keywords,
    variable_keywords,
)
import os


def test_SWC_108_1(json_metadata):
    json_metadata["error_message"] = "Missing state variable visibility"

    CONTRACT_NAME = os.listdir("./contracts")[0]
    in_contract = False
    open_brackets = 0

    # iterate through lines in contract
    with open(f"contracts/{CONTRACT_NAME}", "r") as f:
        lines = remove_whitespace(f)

        # split line into word tokens
        for line in lines:
            words = line.split()

            if words[0] == "contract":
                in_contract = True

            # determine if inside a function
            if in_contract:
                if "{" in words[-1]:
                    open_brackets += 1
                if "}" in words[-1]:
                    open_brackets -= 1

                # finish test when out of contract
                if open_brackets == 0:
                    break

                # if inside contract but outside functions
                if open_brackets == 1:
                    # if state variable
                    if [ele for ele in variable_keywords if (ele in words[0])]:
                        # assert visibility is declared
                        assert any(item in words for item in visibility_keywords)
