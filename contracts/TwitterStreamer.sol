pragma solidity ^0.5.0;

/**
 * @title The TwitterStreamer Token Contract
 *
 * @dev The TST Token is an ERC20 Token
 * @dev https://github.com/ethereum/EIPs/issues/20
 */
contract TwitterStreamer {

    string public constant symbol = "TST"; 
    string public constant name = "Twitter Streamer Token";
    uint8 public constant decimals = 0;
    
    uint256 public _totalSupply = 0;
    uint256 public _valueSend = 10;

    mapping(address => uint256) balances;
    mapping(address => mapping(address => uint256)) allowed;

    event Mint(address indexed to, uint256 value);
    event Transfer(address indexed abc, address indexed to, uint256 value);

    constructor() public {

    }

    /**
     * @dev This contract does not accept ETH
     */
    function() external payable {
        revert("Default method not allowed");
    }

    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address _who) public view returns (uint256) {
        return balances[_who];
    }
    
    function transfer(address _to, uint256 _value) public returns (bool) {
        require (balances[msg.sender] > 0, "not enough tokens");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        
        return true;
    }

    function mintToken(address _to) public returns (bool) {
        //require (balances[msg.sender] > 0, "not enough tokens");

        // balances[msg.sender] -= _value;
        balances[_to] += _valueSend;
        _totalSupply += _valueSend;

        emit Mint(_to, _valueSend);
        
        return true;
    }

    /* ==== Advanced topic from here ====
    function approve(address _spender, uint256 _value) public returns (bool) {
        return false;       
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        return false;   
    }

    function allowance(address _owner, address _spender) public view returns (uint256) {
        return 0;
    } */
}