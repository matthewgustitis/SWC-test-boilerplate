""" main program to test for SWC-100 vulnerabilities """

from config import (
    BROWNIE_CONFIG_FILE_NAME,
    RESULTS_FILE_NAME,
)
from helper_functions import comment_remover
import os, shutil, json, datetime
import urllib.request


# create and enter brownie environment
if os.path.isdir("brownie-folder"):
    shutil.rmtree("brownie-folder")

os.system("mkdir brownie-folder")
os.chdir("brownie-folder")
os.system("brownie init")


# create contract in contracts folder
url = "https://raw.githubusercontent.com/PatrickAlphaC/brownie_simple_storage/main/contracts/SimpleStorage.sol"
file = urllib.request.urlopen(url)
CONTRACT_FILE_NAME = "contracts/" + url[url.rindex("/") + 1 :]
file_text = comment_remover(file)

with open(CONTRACT_FILE_NAME, "w") as f:
    for line in file_text:
        f.write(line)


# insert necessary files into brownie-folder
shutil.copyfile("../copy_files/brownie-config.yaml", BROWNIE_CONFIG_FILE_NAME)
if os.path.isdir("tests"):
    shutil.rmtree("tests")
    shutil.copytree("../copy_files/tests", "tests")


# run SWC-100 tests and load result object
os.system(f"pytest -rP --json-report -v tests/")
pytest_data = None
with open(".report.json", "r") as f:
    pytest_data = json.load(f)


# create and modify json object to output to results file
results_object = {
    "Title": "SWC-100 Test Results",
    "Date": f"{datetime.datetime.now()}",
    "Failed_tests": [],
}

for test in pytest_data["tests"]:
    if test["outcome"] == "failed":
        failure_details = {
            "Test_name": test["nodeid"],
            "Error": test["metadata"]["error_message"],
        }
        results_object["Failed_tests"].append(failure_details)


# output SWC-100 test results
json_object = json.dumps(results_object, indent=4)
with open(RESULTS_FILE_NAME, "w") as outfile:
    outfile.write(json_object)


# tidy up
os.chdir("..")
if os.path.isdir("brownie-folder"):
    shutil.rmtree("brownie-folder")
if os.path.isdir("__pycache__"):
    shutil.rmtree("__pycache__")
if os.path.isdir(".pytest_cache"):
    shutil.rmtree(".pytest_cache")
