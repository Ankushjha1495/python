#This code will give you the factorial of a given number n
n = int(input("Enter a number here:"))
product = 1
for i in range (1, n+1):
    product = product*i
print(f"The factorial of {n} is {product}")