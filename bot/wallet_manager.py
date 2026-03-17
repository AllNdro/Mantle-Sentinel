import os
from web3 import Web3
from eth_account import Account

def get_wallet():

    pk = os.getenv("PRIVATE_KEY")

    return Account.from_key(pk)
