""" tests for general deployment and environment configuration"""

from brownie import accounts
from helper_functions import get_contract

Contract = get_contract()


def test_deploy(json_metadata):
    json_metadata["error_message"] = "Contract failed to deploy"
    account = accounts[0]
    contract = Contract.deploy({"from": account})
    assert contract
