""" tests for general deployment and environment configuration"""

from brownie import SimpleStorage, accounts


def test_deploy(json_metadata):
    json_metadata["error_message"] = "Contract failed to deploy"
    account = accounts[0]
    contract = SimpleStorage.deploy({"from": account})
    assert contract
