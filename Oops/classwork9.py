# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# Create an object of the Circle class and call both methods to display the results.
# class Circle:
#     def __init__(self):
#         self.radius=int(input("Enter the radius : "))
#     def getarea(self):
#         self.area=3.14*(self.radius**(2))
#         print("Area :",self.area)
#     def getperimeter(self):
#         self.perimeter=2*(3.14*self.radius)
#         print("Perimeter ",self.perimeter)
# c=Circle()
# c.getarea()
# c.getperimeter()

# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
class Account:
    def __init__(self):
        self.acctnumber = input("Enter Account Number: ")
        self.acctname = input("Enter Account Holder Name: ")
        self.balance = float(input("Enter Initial Balance: "))

    def withdraw(self):
        amount = float(input("Enter Withdrawal Amount: "))
        self.balance = self.balance - amount
    def deposit(self):
        amount = float(input("Enter Deposit Amount: "))
        self.balance = self.balance + amount

    def showbalance(self):
        print("Account Number:", self.acctnumber)
        print("Account Holder:", self.acctname)
        print("Current Balance:", self.balance)

# a1 = Account()
# a1.withdraw()
# a1.deposit()
# a1.showbalance()
a=Account()
b=Account()
c=Account()
l=[a,b,c]
for i in l:
    print(f"Account no : {i.acctnumber} Name : {i.acctname} Balance : {i.balance} ")