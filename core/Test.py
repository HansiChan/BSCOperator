import json

import numpy as np
from web3 import Web3

# 测试网
w3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545'))
# 主网
# w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org:443'))
private_key = ''
account = w3.eth.account.from_key(private_key)
np.set_printoptions(suppress=True)


def getAddress():
    print("address:" + str(account.address))
    return account.address


def getBNBBalance():
    balance = exchangeWei(w3.eth.get_balance(account.address))
    print("balance:" + str(balance))
    return balance


def getTokenBalance(concat):
    concat = w3.toChecksumAddress(concat)
    abi = '''
    [{
    "type":"function",
    "name":"balanceOf",
    "constant":true,
    "payable":false,
    "inputs":[{"name":"","type":"address"}],
    "outputs":[{"name":"","type":"uint256","value":"0"}]
    }]
    '''
    abi = json.loads(abi)
    source_code = w3.eth.getCode(concat)
    contract = w3.eth.contract(abi=abi, address=concat, bytecode=source_code)
    balance = exchangeWei(contract.functions.balanceOf(account.address).call())
    print("balance:" + str(balance))
    print(contract.functions.balanceOf(account.address).call())
    return balance


def exchangeWei(balance):
    return w3.fromWei(balance, 'ether')


def getGas():
    return exchangeWei(w3.eth.gas_price)


def getTransaction(trans_hash):
    return w3.eth.get_transaction(trans_hash)


def sendTransaction(from_acc, to_acc, value):
    nonce = w3.eth.getTransactionCount(account.address)

    trans = {'nonce': nonce, 'to': to_acc,
             'from': from_acc,
             'value': w3.toWei(value, "ether"),
             'gas': 21000,
             'gasPrice': w3.toWei('10', 'gwei')
             }
    print("trans:" + str(trans))
    signed_tx = w3.eth.account.signTransaction(trans, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print("转账成功,hash:" + w3.toHex(tx_hash))
    return tx_hash


if __name__ == '__main__':
    busd = '0xfa0e9ed1eea6c03773f0ee720f4cd8c47f31ee63'
    to_address = '0x19b22f73f63F00206E21f86ac78a77f4f76850e4'
    getTokenBalance(busd)
    # sendTransaction(account.address, to_address, 1)
