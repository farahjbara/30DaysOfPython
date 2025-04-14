class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number # Encapsulated as a protected attribute
        self._account_holder = account_holder # Encapsulated as a protected attribute
        self._balance = balance # Encapsulated as a protected attribute
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print (f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")
    def withdraw (self, amount):
        if amount > 0 <= self._balance:
            self._balance -= amount
            print (f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    def get_balance(self):
        return self._balance #Encapsulation allows controlled access 
    def account_info(self):
        return f"Account: {self._account_number}, Holder : {self._account_holder}, Balance: ${self._balance}"
class SavingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self._interest_rate = interest_rate
    def apply_interest(self):
        interest = self._balance * self._interest_rate 
        self._balance += interest 
        print(f"Applied interest: ${interest}. New balance: ${self._balance}")
# Create a Saving account 
saving_account = SavingAccount("123456789", "John Doe", 1000)
# Perform transactions and display account information 
print("Account information:")
print(saving_account.account_info())
saving_account.deposit(500)
saving_account.withdraw(200)
saving_account.apply_interest()
print("Account information after transactions:")
print(saving_account.account_info())
'''
In this program:
 The Account class encapsulates account details such as account_number,
account_holder, and balance. These attributes are marked as protected. The class
provides methods to deposit, withdraw, get the balance, and retrieve account information.
 The SavingsAccount class is a subclass of Account that adds an interest_rate
attribute and a method to apply interest. It inherits the encapsulated attributes and
behaviors from the base class.
 We create a SavingsAccount instance, perform transactions (deposit, withdrawal, and
interest application), and display account information.
'''
### Test :
class Vehicle:
    def __init__(self, type):
       self._type= type
    def move(self):
       print (f"The vehicle moves")
class Bike(Vehicle):
    def __init__(self, wheels, type):
       self._wheels = wheels
       super().__init__(type) # Call Vehicle's constructor
    def move(self):
        super().move()
        print(f"The bike has {self._wheels} wheels.")
        
my_bike = Bike("bike",2)
my_bike.move()