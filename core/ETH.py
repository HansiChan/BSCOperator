import os

from web3 import Web3


def start_node(db='../eth-test/db/', port='30303', rpcport='8545'):
    cmdOrder = 'geth --datadir ' + db + ' --rpc --rpcapi "eth,net,web3,personal,admin,txpool,debug,miner"' \
                                        ' --port ' + port + ' --rpcport ' + rpcport \
               + ' --nodiscover --rpccorsdomain "*" --allow-insecure-unlock --ipcdisable'
    os.system(cmdOrder)


class ETH(object):

    def __init__(self, ip, rpcport):
        # 连接本地以太坊节点
        self.w3 = Web3(Web3.HTTPProvider('http://' + ip + ':' + rpcport, request_kwargs={'timeout': 60}))

    # 返回当前所有账户
    def getAddrs(self):
        return self.w3.eth.accounts

    # 返回指定地址的余额
    def getBalance(self, addr):
        balance = self.w3.fromWei(self.w3.eth.getBalance(addr), 'ether')
        return balance

    # 返回当前节点的 enode 信息
    def getEnode(self):
        return self.w3.geth.admin.node_info()['enode']

    # 返回当前节点数
    def peers(self):
        return self.w3.geth.admin.peers()

    # 当前节点添加节点
    def addPeer(self, enode):
        return self.w3.geth.admin.add_peer(enode)

    # # 开始挖矿
    # def minerStart(self):
    #     self.w3.geth.miner.start(1)
    # # 结束挖矿
    # def minerStop(self):
    #     self.w3.geth.miner.stop()


if __name__ == '__main__':
    start_node()
    print("start")
    my_eth = ETH('30303', '8545')
    print('address:' + my_eth.getAddrs()[0])
