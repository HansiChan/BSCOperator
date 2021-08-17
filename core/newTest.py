from web3 import Web3

# w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545'))

# 转出账户
my_address = "0x2F42fCd8D06A840C242814ea5AaAa60699C3D69c"
my_pkey = ""  # 私钥

from_add = Web3.toChecksumAddress(my_address)
nonce = w3.eth.getTransactionCount(from_add)

to_add_s = Web3.toChecksumAddress("0x19b22f73f63F00206E21f86ac78a77f4f76850e4")

tx = {
    'nonce': nonce,
    'to': to_add_s,
    'value': w3.toWei(0.5, 'ether'),
    'gas': 21000,
    'gasPrice': w3.toWei('5', 'gwei'),
}
signed_tx = w3.eth.account.signTransaction(tx, my_pkey)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(w3.toHex(tx_hash))
print("转账BNB成功")
