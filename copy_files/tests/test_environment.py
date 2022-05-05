""" tests for general deployment and environment configuration"""

from brownie import accounts
import os
import importlib


CONTRACT_NAME = os.listdir("./contracts")[0]
CONTRACT_NAME = CONTRACT_NAME.split(".")[0]
Contract = getattr(importlib.import_module("brownie"), CONTRACT_NAME)


def test_deploy(json_metadata):
    json_metadata["error_message"] = "Contract failed to deploy"
    account = accounts[0]
    contract = Contract.deploy({"from": account})
    assert contract
