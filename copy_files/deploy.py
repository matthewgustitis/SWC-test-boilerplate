""" deploy contract onto chosen test chain """

from brownie import accounts, SimpleStorage


def deploy_contract():
    account = accounts[0]
    SimpleStorage.deploy({"from": account})


def main():
    deploy_contract()
