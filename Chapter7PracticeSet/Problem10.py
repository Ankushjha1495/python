#This code will print the opposite table of any given number n
n = int(input("Enter a number here:"))
for i in range(1,11):
    print(f"{n} X {11-i} = {n* (11-i)}")