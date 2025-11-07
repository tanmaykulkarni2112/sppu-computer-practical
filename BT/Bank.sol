// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank{
    // dpv
    mapping(address => uint) private balances;

    function createAccount() public {
        balances[msg.sender] = 0;
    }

    function depositeEth(uint amount) public {
        balances[msg.sender] += amount;
    }

    function withdrawEth(uint amount) public {
        require(amount <= balances[msg.sender], "Insufficient");
        balances[msg.sender] -= amount;
    }

    function transferEth(address receiver, uint amount) public {
        require(amount <= balances[msg.sender], "Insufficient");
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
    }

    function getBalance() public view returns(uint eth) {
        return balances[msg.sender];
    }
}