from brownie import (
    network,
    accounts,
    config,
    Contract,
    interface
)

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local', 'mainnet-fork', 'mainnet-fork-dev']

DECIMALS = 8
STARTING_PRICE = 400_000_000_000  # 4000 USD + 8 decimals


def get_account(index=None, id=None):
    # accounts[0]
    # accounts.load("id")
    # accounts.add("env")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]  # pull from our development accounts
    return accounts.add(config['wallets']['from_key'])
