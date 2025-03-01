a = int(input("Enter Your age: "))
#if statement number 1
if(a%2 == 0):
    print("The number is even")
#if statement number 2
if(a>18):
    print("Your are above the age of Consent")
elif(a<0):
    print("You are entering an invalid Age")
else:
    print("You are below the age of consent")
    
print("End of Program")        