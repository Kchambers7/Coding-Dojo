from bankAccount import BankAccount


class User:

def __init__(self, name, email, account, savings, checking):
     self.name = name 
     self.email = email 
     self.account = account 
     self.savings = savings 
     self.checking = checking


     def make_deposit (self, amount, type):
          self.accounts[type].deposit(amount) 
         

        def make_withdrawal (self, amount, type):
            self.accounts[type].withdrawl(amount)

    def display_user_balance(self):
        self.accounts.display_account_info()

savings = BankAccount(.1, 10000)
checking = BankAccount(.1, 5000)

Alden = User("Alden", "ac@gmail.com", savings, checking)