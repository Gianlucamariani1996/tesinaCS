pragma solidity ^0.4.2;

contract KotET {   
  address public king;  
  uint public claimPrice = 100;
  address owner;

  function KotET() payable{ 
    owner = msg.sender;  
    king = msg.sender;
    if (msg.value<1 ether) throw;
  }
   
  function sweepCommission(uint amount)  {
    bool res = owner.send(amount);
  }  

  function() payable {     
    if (msg.value < claimPrice) throw;
    
    uint compensation = calculateCompensation();
    bool res = king.send(compensation);  
    king = msg.sender;        
    claimPrice = calculateNewPrice();    
  }  
  
  function calculateCompensation() private returns(uint) {
    return claimPrice+100;
  }
  
  function calculateNewPrice() private returns(uint) {
    return msg.value+200;
  }
}

contract Bob {
  uint public count;
    
  function unseatKing(address king, uint w)payable{
    bool res = king.call.value(w)();
  }
    
  function() payable{
      count++;
  }
  // Helper function to check the balance of this contract
  function getBalance() public view returns (uint) {
      return address(this).balance;
  }
}

contract Alice {
    
  function unseatKing(address king, uint w)payable{
    bool res = king.call.value(w)();
  }
    
  function() payable{
      
  }
  // Helper function to check the balance of this contract
  function getBalance() public view returns (uint) {
      return address(this).balance;
  }
}