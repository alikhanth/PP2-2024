class Account: 
    owner = "" 
    balance = 0 
    def __init__(self,owner,balance): 
        self.owner = owner 
        self.balance = balance 
    def deposit(self,amount): 
        if amount > 0: 
            self.balance += amount 
            print(f"Deposit {amount}. New balance {self.balance}") 
        else: 
            print("Invalid deposit amount") 
    def withdraw(self,amount): 
        if amount > 0 and amount <= self.balance: 
            self.balance -= amount
            print(f"Withdraw {amount}. New balance {self.balance}") 
        else: 
            print("Invalid withdrawal amount") 
owner = str(input()) 
balance = int(input()) 
account = Account(owner,balance) 
amount = int(input())
account.deposit(amount) 
withdraw = int(input()) 
account.withdraw(withdraw)

