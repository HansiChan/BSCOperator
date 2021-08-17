import requests
from web3 import Web3
import time
import re

session = requests.session()
api_url = "https://api.bscscan.com/api"


def getBNB_BALANCE(address, api_key):
    """
    获取BNB余额
    :return: BNB余额
    """
    url = api_url + "?module=account&action=balance&address=%s&apikey=%s" % (address, api_key)
    bnb_balance = session.get(url).text
    print(bnb_balance)


def getGas(api_key):
    url = api_url + "?module=proxy&action=eth_gasPrice&apikey=%s" % api_key
    gas = session.get(url).text
    print(gas)


def start_node():
    w3 = Web3(Web3.IPCProvider('https://mainnet.infura.io/v3/<infura-project-id>'))


if __name__ == '__main__':
    my_address = "0x2F42fCd8D06A840C242814ea5AaAa60699C3D69c"
    my_api_key = ""
    getBNB_BALANCE(my_address, my_api_key)
    getGas(my_api_key)
