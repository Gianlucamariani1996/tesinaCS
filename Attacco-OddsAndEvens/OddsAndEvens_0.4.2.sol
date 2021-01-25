pragma solidity ^0.4.2;

contract OddsAndEvens{

  struct Player {
    address addr;
    uint number;
  }
  
  Player[2] private players;  
  uint8 tot;
  address owner;

  function OddsAndEvens() {
    owner = msg.sender;
  }
  
  function play(uint number) payable{
    if (msg.value != 1 ether) throw;
    
    players[tot] = Player(msg.sender, number);
    tot++;
    
    if (tot==2) andTheWinnerIs();
  }
  
  function andTheWinnerIs() private {
    bool res ;
    uint n = players[0].number+players[1].number;
    if (n%2==0) {
      res = players[0].addr.send(1800 finney);
    }
    else {
      res = players[1].addr.send(1800 finney);
    }
        
    delete players;
    tot=0;
  }
  
  function getProfit() payable{
    if(msg.sender!=owner) throw;
    bool res = msg.sender.send(this.balance);
  }
  
  // Helper function to check the balance of this contract
  function getBalance() public view returns (uint) {
      return address(this).balance;
  }

}
