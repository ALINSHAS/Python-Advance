# File read
# File write
# File append
# File search
# File remove
# Exit
def fileread():
    filename=input("Enter the file name : ")
    f=open(filename,"r")
    content=f.read()
    print(content)
    f.close()

def filewrite():
    filename=input("Enter the file name : ")
    content=input("Enter the content you want to enter :\n")
    f=open(filename,"w")
    f.write(content)
    f.close()

def fileappend():
    filename=input("Enter the file name : ")
    content=input("Enter your content : ")
    f = open(filename, "a")
    f.write(content)
    f.close()

def filesearch():
    filename=input("Enter the file name : ")
    word=input("Enter a word to search : ")
    f=open(filename,"r")
    r=f.read()
    if word in r:
        print("Found the word")
    else:
        print("Not found")

def fileremove():
    filename=input("Enter the file name")
    import os
    os.remove(filename)
    



while(1):
    print("1.File read ")
    print("2.File write")
    print("3.File append ")
    print("4.File search")
    print("5.File remove")
    print("6.Exit")

    ch=int(input("Enter your choice : "))

    if ch == 1:
        fileread()
    elif ch == 2:
        filewrite()
    elif ch == 3:
        fileappend()
    elif ch == 4:
        filesearch()
    elif ch == 5:
        fileremove()
    else:
        exit()