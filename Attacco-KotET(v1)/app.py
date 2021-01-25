# Definisco un oggetto contratto bob a partire dall'interfaccia e dal bytecode
bobContract = web3.eth.contract(abi=bobInterfaceJS, bytecode=bobBytecode)
# Costruisco la transazione per fare il deploy del contratto bob
contract_data = bobContract.constructor().buildTransaction()
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_bob = web3.eth.contract(address=txn_receipt.contractAddress, abi=bobInterfaceJS)