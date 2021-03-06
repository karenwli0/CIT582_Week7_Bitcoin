from web3 import Web3
from hexbytes import HexBytes

IP_ADDR = '18.188.235.196'
PORT = '8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

if w3.isConnected():
    print()
    # print("Connected to Ethereum node")
else:
    print("Failed to connect to Ethereum node!")


def get_transaction(tx):
    transaction = w3.eth.get_transaction(tx)  # YOUR CODE HERE
    return transaction


# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    transaction = get_transaction(tx)
    gas_price = transaction['gasPrice']
    return gas_price


def get_gas(tx):
    transaction = w3.eth.get_transaction_receipt(tx)
    gas = transaction['gasUsed']
    return gas


def get_transaction_cost(tx):
    tx_cost = get_gas_price(tx) * get_gas(tx)
    return tx_cost


def get_block_cost(block_num):
    transactions = w3.eth.get_block(block_num)['transactions']
    block_cost = 0
    for transaction in transactions:
        block_cost += get_transaction_cost(transaction)
    return block_cost


# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    transactions = w3.eth.get_block(block_num)['transactions']
    max_transaction_cost = 0
    max_tran = 0
    for transaction in transactions:
        this_tran_cost = get_transaction_cost(transaction)
        if max_transaction_cost < this_tran_cost:
            max_transaction_cost = this_tran_cost
            max_tran = transaction
    max_tx = HexBytes(max_tran)  # YOUR CODE HERE
    return max_tx
