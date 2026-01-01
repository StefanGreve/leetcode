from typing import List

# PROBLEM STATEMENT
# https://leetcode.com/quest/maths-quest/quiz/simple-bank-system/?envType=problem-list-v2&envId=maths-m2-assignment
#
# You have been tasked with writing a program for a popular bank that will automate
# all its incoming transactions (transfer, deposit, and withdraw). The bank has
# n accounts numbered from 1 to n. The initial balance of each account is stored
# in a 0-indexed integer array balance, with the (i + 1)th account having an
# initial balance of balance[i].
#
# Execute all the valid transactions. A transaction is valid if:
# - The given account number(s) are between 1 and n, and
# - The amount of money withdrawn or transferred from is less than or equal to the
#   balance of the account.
#
# Implement the Bank class:
#
# - Bank(long[] balance) Initializes the object with the 0-indexed integer array
#   balance.
# - boolean transfer(int account1, int account2, long money) Transfers money dollars
#   from the account numbered account1 to the account numbered account2. Return
#   true if the transaction was successful, false otherwise.
# - boolean deposit(int account, long money) Deposit money dollars into the account
#   numbered account. Return true if the transaction was successful, false otherwise.
# - boolean withdraw(int account, long money) Withdraw money dollars from the
#   account numbered account. Return true if the transaction was successful,
#   false otherwise.
#
# CONSTRAINTS
# n == balance.length
# 1 <= n, account, account1, account2 <= 105
# 0 <= balance[i], money <= 1012
# At most 104 calls will be made to each function transfer, deposit, withdraw.
#
# EXAMPLES
# Input     ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
#           [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
# Output    [null, true, true, true, false, false]

class Bank:
    def __init__(self, balance: List[int]):
        self.accounts = balance

    def __validate_account(self, account: int) -> bool:
        if (account - 1 < 0 or account > len(self.accounts)):
            return False

        return True

    def __validate_money(self, money: int) -> bool:
        return money > 0

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (not self.__validate_account(account1) or not self.__validate_account(account2)):
            return False

        if (not self.__validate_money(money)):
            return False

        if (self.accounts[account1 - 1] >= money):
            self.accounts[account1 - 1] -= money
            self.accounts[account2 - 1] += money
            return True

        return False

    def deposit(self, account: int, money: int) -> bool:
        if (not self.__validate_account(account)):
            return False

        if (not self.__validate_money(money)):
            return False

        self.accounts[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if (not self.__validate_account(account)):
            return False

        if (not self.__validate_money(money)):
            return False

        if (self.accounts[account - 1] >= money):
            self.accounts[account - 1] -= money
            return True

        return False

if __name__ == '__main__':
    # example
    bank = Bank([10, 100, 20, 50, 30])
    bank.withdraw(3, 10)    # $10
    bank.transfer(5, 1, 20) # $20
    bank.deposit(5, 20)     # True
    bank.transfer(3, 4, 15) # False
    bank.withdraw(10, 50)   # False
