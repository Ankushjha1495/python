#This code tells that username enter by you had a length of 10 or greater
#if username length is greater than 10 than code will tell accordingly
Username = input("Enter Your username")
lengthUsername = len(Username)
if(lengthUsername<10):
    print("This username contains less than 10 characters")

else:
    print("This username contains more than 10 characters")    
