#First Method to run this program
def GreatestNumber(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print(f"{n1} is the greatest Number")
    elif(n2>n1 and n2>n3):
        print(f"{n2} is the greatest Number")
    elif(n3>n2 and n3>n1):
        print(f"{n3} is the greatest Number")

n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))
GreatestNumber(n1,n2,n3)  

#Second method to run this program
n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))

def GreatestNumber():
    if(n1>n2 and n1>n3):
        print(f"{n1} is the greatest Number")
    elif(n2>n1 and n2>n3):
        print(f"{n2} is the greatest Number")
    elif(n3>n2 and n3>n1):
        print(f"{n3} is the greatest Number")
GreatestNumber()             
