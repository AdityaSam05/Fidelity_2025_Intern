# Create a class called customer that contains name and balance. And the methods are deposit and withdraw

class Customer:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            print(amount)
    def withdraw(self,amount):
        if(self.balance>amount>0):
            self.balance-=amount
            print(amount)
        elif(amount>self.balance):
            print("Insufficient money")
    def check_balance(self):
        return self.balance
    
c1=Customer("Sarthak",100)
print(c1)
c1.deposit(40)
c1.withdraw(70)
c1.withdraw(100)
print("Balance--->",c1.check_balance())
        