pragma solidity ^0.5.0;


contract HelloWorld {

    string public message;
    uint256 public number;    
    
    event NewMessage(address indexed from, string message);
    event NewNumber(address indexed from, uint256 number);

    constructor() public {
    }

    function setMessage(string memory _message) public returns (bool) {
        message = _message;
        emit NewMessage(msg.sender, message);
        return true;
    }

    function setNumber(uint256 _number) public returns (bool) {
        number = _number;
        
        emit NewNumber(msg.sender, number);
        return true;
    }

}
