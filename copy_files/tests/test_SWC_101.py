""" tests for SWC 101 vulnerabilities """


from brownie import accounts, SimpleStorage


def test_SWC_101_1(json_metadata):
    json_metadata["error_message"] = "Initial Value incorrect"
    account = accounts[0]
    contract = SimpleStorage.deploy({"from": account})
    starting_value = contract.retrieve()
    expected = 1
    assert starting_value == expected


def test_SWC_101_2(json_metadata):
    json_metadata["error_message"] = "Some error desription"
    account = accounts[0]
    contract = SimpleStorage.deploy({"from": account})
    starting_value = contract.retrieve()
    expected = 0
    assert starting_value == expected
