#
# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()

class Movie:
    def __init__(self):
        self.Mname =input("Enter Movie name: ")
        self.Myear=input("Enter Movie year: ")
        self.Language=input("Enter Movie language: ")
        self.Director=input("Enter Director Name: ")
        self.Rating=""
    def display_details(self):

        print(f"Movie Name: {self.Mname}  Year: {self.Myear}  Language: {self.Language}  Director: {self.Director}  ")
        if (self.Rating == ""):
            print("Rating is empty")
        else:
            self.Rating = float(self.Rating)
            print(f"Rating: {self.Rating}")

    def update_rating(self):
        self.Rating=input("Enter Rating: ")


m=Movie()
m.display_details()
m.update_rating()
m.display_details()







# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.
#

class Vehicle:
    def __init__(self):
        self.brand=input("Enter the brand of the vehicle: ")
        self.model=input("Enter the model of the vehicle: ")
        self.color=input("Enter the color of the vehicle: ")
        self.year=input("Enter the year of the vehicle: ")
    def display(self):
        print(f'Brand : {self.brand} \nModel: {self.model} \nColor: {self.color} \nYear: {self.year}')
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.mileage=input("Enter the mileage of the car: ")
    def display(self):
        super().display()
        print(f'Mileage: {self.mileage}')


class Bike(Vehicle): 
    def __init__(self):
        super().__init__()
        self.cc=input("Enter ther CC: ")
    def display(self):
        super().display()
        print(f'CC: {self.cc}')


c=Car()
c.display()
b=Bike()
b.display()







##3 Create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.




#
#4 create an abstract class Shape with abstract methods get_area() and get_perimeter()
# create two subclasses
#  -Rectangle
#  -Square
#
#  -Each class should calculate area() and perimeter() differently.
class Shape:
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
class Rectangle(Shape):

    def __init__(self):
        self.length=int(input("Enter the length of the rectangle: "))
        self.breadth=int(input("Enter the breadth of the rectangle: "))
    def get_area(self):
        print("Area:",self.length*self.breadth)
    def get_perimeter(self):
        print("Perimeter:",2*(self.length+self.breadth))




class Square(Shape):
    def __init__(self):
        self.length=int(input("Enter the length of the square: "))
    def get_area(self):
        print("Area:",self.length*self.length)
    def get_perimeter(self):
        print("Perimeter:",4*self.length)

r=Rectangle()
r.get_area()
r.get_perimeter()
s=Square()
s.get_area()
s.get_perimeter()