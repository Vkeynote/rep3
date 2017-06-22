class BankAccount(object):
    def __init__(self, balance = 3000):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
