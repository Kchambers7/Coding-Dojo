from bankAccount import BankAccount


class User:

def __init__(self, name, email, account):
     self.name = name 
     self.email = email 
     self.account = account 

savings = BankAccount(.1, 10000)

Alden = User("Alden", "ac@gmail.com", savings)