def factorial(n):
    if(n<0):
        return "This number does not have any factorial"
    if(n == 1 or n == 0):
        return 1
    return n*factorial(n-1)
a = int(input("Enter the number:"))
print(F"The factorial of {a} is {factorial(a)}")