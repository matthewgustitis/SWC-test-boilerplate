""" test file """

from brownie import SimpleStorage, accounts

"""
def test_deploy():
    account = accounts[0]
    contract = SimpleStorage.deploy({"from": account})
    assert contract, "Error: contract failed to deploy"
"""


def test_deploy(json_metadata):
    json_metadata["error_message"] = "Contract failed to deploy"
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 1
    assert starting_value == expected
