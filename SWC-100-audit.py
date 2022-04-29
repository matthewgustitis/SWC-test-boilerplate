import urllib.request
from config import (
    CONTRACT_FILE_NAME,
    DEPLOY_FILE_NAME,
    BROWNIE_CONFIG_FILE_NAME,
    RESULTS_FILE_NAME,
    TEST_FILE_NAME,
)
import os
import shutil
import datetime


# create and enter brownie environment
if os.path.isdir("brownie-folder"):
    shutil.rmtree("brownie-folder")

os.system("mkdir brownie-folder")
os.chdir("brownie-folder")
os.system("brownie init")


# create contract in contracts folder
url = "https://raw.githubusercontent.com/PatrickAlphaC/brownie_simple_storage/main/contracts/SimpleStorage.sol"
file = urllib.request.urlopen(url)

with open(CONTRACT_FILE_NAME, "w") as f:
    for line in file:
        decoded_line = line.decode("utf-8")
        f.write(decoded_line)


# insert necessary files into brownie-folder
shutil.copyfile("../copy_files/deploy.py", DEPLOY_FILE_NAME)
shutil.copyfile("../copy_files/brownie-config.yaml", BROWNIE_CONFIG_FILE_NAME)
if os.path.isdir("tests"):
    shutil.rmtree("tests")
    shutil.copytree("../copy_files/tests", "tests")


# run SWC-100 tests and print results
with open(f"../{RESULTS_FILE_NAME}", "w") as f:
    f.write("SWC AUDIT TEST RESULTS: \n\n")
    f.write(f"{datetime.datetime.now()} \n\n\n")

    # THIS TO BE CHANGED TO CREATE TESTRESULTOBJECTS THAT CAN BE PUSHED TO API OR WHATEVER
    for filename in os.listdir("tests"):
        f.write(f"TEST: {filename}\n")
        f.write("LIST OF ERRORS AND OVERALL STATUS FROM THIS TEST\n\n")
        os.system(f"pytest tests/{filename}")


# tidy up
os.chdir("..")
if os.path.isdir("brownie-folder"):
    shutil.rmtree("brownie-folder")
if os.path.isdir("__pycache__"):
    shutil.rmtree("__pycache__")
if os.path.isdir(".pytest_cache"):
    shutil.rmtree(".pytest_cache")
