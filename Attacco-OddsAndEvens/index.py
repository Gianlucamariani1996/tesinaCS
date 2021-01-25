from web3 import Web3
import json

web3 = Web3(Web3.HTTPProvider('http://node:8545'))
if (web3.isConnected()):
    print("Connessione con il nodo riuscita" + "\n")
else:
    print("Connessione con il nodo fallita" + "\n")

oddsAndEvensInterface = [
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
		"inputs": [],
		"name": "getProfit",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "number",
				"type": "uint256"
			}
		],
		"name": "play",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	}
]
oddsAndEvensInterfaceJS = json.dumps(oddsAndEvensInterface) 

oddsAndEvensBytecode = "6060604052341561000f57600080fd5b33600460016101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506104858061005f6000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806312065fe01461005c578063679dffb4146100855780636898f82b1461008f575b600080fd5b341561006757600080fd5b61006f6100a7565b6040518082815260200191505060405180910390f35b61008d6100c6565b005b6100a56004808035906020019091905050610175565b005b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000600460019054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561012457600080fd5b3373ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050905050565b670de0b6b3a76400003414151561018b57600080fd5b60408051908101604052803373ffffffffffffffffffffffffffffffffffffffff168152602001828152506000600460009054906101000a900460ff1660ff166002811015156101d757fe5b6002020160008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550602082015181600101559050506004600081819054906101000a900460ff168092919060010191906101000a81548160ff021916908360ff160217905550506002600460009054906101000a900460ff1660ff16141561028557610284610288565b5b50565b6000806000600160028110151561029b57fe5b60020201600101546000806002811015156102b257fe5b600202016001015401905060006002828115156102cb57fe5b06141561034c576000806002811015156102e157fe5b6002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc6718fae27693b400009081150290604051600060405180830381858888f1935050505091506103c3565b6000600160028110151561035c57fe5b6002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc6718fae27693b400009081150290604051600060405180830381858888f1935050505091505b6000806103d091906103f0565b6000600460006101000a81548160ff021916908360ff1602179055505050565b50600080820160006101000a81549073ffffffffffffffffffffffffffffffffffffffff0219169055600182016000905550600201600080820160006101000a81549073ffffffffffffffffffffffffffffffffffffffff0219169055600182016000905550505600a165627a7a723058206944208885420a684a04fc08323d8fe0432bcb6e63344fc608083a7624b276950029"

accounts = web3.eth.accounts
# Set dell'account con il quale farò i deploy
web3.eth.defaultAccount = web3.eth.accounts[0]

# Definisco un oggetto contratto oddsAndEvens a partire dall'interfaccia e dal bytecode
oddsAndEvensContract = web3.eth.contract(abi=oddsAndEvensInterfaceJS, bytecode=oddsAndEvensBytecode)
# Costruisco la transazione per fare il deploy del contratto oddsAndEvens
contract_data = oddsAndEvensContract.constructor().buildTransaction({'from': accounts[0]})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_oddsAndEvens = web3.eth.contract(address=txn_receipt.contractAddress, abi=oddsAndEvensInterfaceJS)
# Address, balance e functions di oddsAndEvens
print("L'account[0] ha pubblicato il contratto oddsAndEvens: " + str((contract_oddsAndEvens.address)) 
+ "\nil cui bilancio iniziale è: " + str(web3.eth.getBalance(contract_oddsAndEvens.address)) + "\ned offre le seguenti funzioni:" + "\n"
+ str(contract_oddsAndEvens.all_functions()) + "\n")

# Bilancio di Alice prima di giocare
print("Bilancio Alice (account[1])):\n" + str(web3.eth.getBalance(accounts[1])) + "\n")
# Alice gioca mettendo il numero 10
print("Alice (account[1]) gioca un numero: \n")
contract_oddsAndEvens.functions.play(10).transact({'from': accounts[1], 'value': 1000000000000000000})
# Stampa per dire che Alice ha giocato
print("Alice (account[1]) ha giocato:\n" + str(10) + "\n")
# Bilancio di Alice prima di giocare
print("Bilancio di Alice (account[1]) (dopo aver giocato):\n" + str(web3.eth.getBalance(accounts[1])) + "\n")

# Bilancio del contratto oddsAndEvens
print("Bilancio del contratto oddsAndEvens(dopo che Alice (account[1]) ha giocato):\n" + str(web3.eth.getBalance(contract_oddsAndEvens.address)) + "\n")

# Bilancio di Bob prima di giocare
print("Bilancio Bob prima di giocare:\n" + str(web3.eth.getBalance(accounts[2])) + "\n")

# Adesso Bob può vedere il numero giocato da Alice visto che la blockchain è pubblica
y = web3.eth.getStorageAt(contract_oddsAndEvens.address, 1)
# Converto da HexBytes (visto con print(type(y))) a int
y = web3.toInt(y)
print("A questo punto Bob (account[2]) legge che il numero giocato da Alice e salvato nella blockchain è:\n" + str(y) + "\n")

# Dato che Bob è il secondo a giocare e sa che il contratto paga il secondo giocatore se la somma è dispari
if(y%2==0):
	z = 1
else: 
	z = 0
print("A questo punto visto che Bob ha letto il numero " + str(y) + " gioca il numero " + str(z) + "\n")
# Bob gioca mettendo il numero z
contract_oddsAndEvens.functions.play(z).transact({'from': accounts[2], 'value': 1000000000000000000})
# Bilancio di Bob prima di giocare
print("Bob ha vinto !!! Bilancio Bob(dopo aver giocato):\n" + str(web3.eth.getBalance(accounts[2])) + "\n")
# Bilancio del contratto oddsAndEvens
# Si aggiorna, sono wei ricorda
print("Bilancio del contratto (finale):\n" + str(web3.eth.getBalance(contract_oddsAndEvens.address)) + "guei\n")
