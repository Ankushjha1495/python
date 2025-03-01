a = int(input("Enter Your age: "))
#if else statement
if(a>18):
    print("Your are above the age of Consent")
elif(a<0):
    print("You are entering an invalid Age")
elif(a==0):
    print("You are entering 0 which is not a valid age")
else:
    print("You are below the age of consent")
    
print("End of Program")        