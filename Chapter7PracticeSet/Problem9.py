'''n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    if(i ==1 or i ==n):
        print("*"*n, end= "")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")'''









n =int(input("Enter the Number of rows: "))
for i in range(1,n+1):
    if(i == 1 and i == n):
        star = n*i
    else:
        star = n*(n-2)    
print("*"*star)        








