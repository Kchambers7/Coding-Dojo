class BankAccount:

   accounts = []
    
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate 
        self.balance = balance
        BankAccount.accounts.append(self)
        def deposit(self):
        
        def deposit (self, amount):
          self.balance += amount 
          return self 

        def withdrawal (self, amount):
            if(self.balance >= amount):
              self.balance -= amount
            else:
              print("Insufficient funds: Charging a $5 fee")
              self.balance -= 5
            return self

        def display_account_info(self):
             print(f"Your balance is: $(self.balance)")
             return self

        def yield_interest(self): 
            if(self.balance > 0):
                 self.balance += self.balance * self.interest_rate 
            return self

        @classmethod
        def display_all_account_info(cls):
          for account in cls.accounts:
              print("Interest Rate: (account.interest_rate), Account balance: (account.balance)" )



    acct1 = BankAccount (0, 1, 1000)
    acct2 = BankAccount (0, 1, 10000) 