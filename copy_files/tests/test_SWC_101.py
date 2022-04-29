from brownie import SimpleStorage, accounts


def test_deploy():
    account = accounts[0]
    contract = SimpleStorage.deploy({"from": account})
    starting_value = contract.retrieve()
    expected = 0
    assert starting_value == expected, "Error: Initial value incorrect"


def test_updating_storage():
    account = accounts[0]
    contract = SimpleStorage.deploy({"from": account})
    expected = 15
    txn = contract.store(expected, {"from": account})
    txn.wait(1)
    assert expected == contract.retrieve(), "Error: updating value failed"
