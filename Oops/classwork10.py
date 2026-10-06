class Student:
    def __init__(self):
        self.rollno = int(input("Enter Roll Number: "))
        self.name = input("Enter Name: ")
        self.marks = float(input("Enter Marks: "))

    def updatemarks(self):
        self.marks = float(input("Enter New Marks: "))

    def display(self):
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)


student = []

while True:
    print("\nMenu Driven Program")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All Student Details")
    print("4. Search Student by Roll Number")
    print("5. Delete Student")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        s = Student()
        student.append(s)
        print("Student Added Successfully")

    elif ch == 2:
        roll = int(input("Enter Roll Number: "))

        for i in student:
            if i.rollno == roll:
                i.updatemarks()
                break

        else:
            print("Student Not Found")

    elif ch == 3:
        for i in student:
            i.display()
            
    elif ch == 4:
        roll = int(input("Enter Roll Number: "))

        for i in student:
            if i.rollno == roll:
                i.display()
                break

        else:
            print("Student Not Found")

    elif ch == 5:
        roll = int(input("Enter Roll Number: "))

        for i in student:
            if i.rollno == roll:
                student.remove(i)
                print("Student Deleted")
                break

        else:
            print("Student Not Found")

    else:
        exit()