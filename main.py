from web3 import Web3 
from contract_info import abi, address_contract 
from web3.middleware import geth_poa_middleware 
 
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")) 
w3.middleware_onion.inject(geth_poa_middleware, layer=0) 
 
accounts = w3.eth.accounts 
 
for account in accounts: 
    balance = w3.eth.get_balance(account) 
    print(f"Аккаунт: {account}, Баланс: {w3.from_wei(balance, 'ether')} ether")
