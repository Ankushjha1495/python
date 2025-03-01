#This code tells that which number out of 4 is the greatest
num1 = int(input("Enter No.1:"))
num2 = int(input("Enter No.2:"))
num3 = int(input("Enter No.3:"))
num4 = int(input("Enter No.4:"))
if(num1>num2 and num1>num3 and num1>num4):
    print("Num1 is the Greatest Number:", num1)

elif(num2>num1 and num2>num3 and num2>num4):
    print("Num2 is the Greatest Number:", num2)

elif(num3>num2 and num3>num1 and num3>num4):
    print("Num3 is the Greatest Number:", num3)

elif(num4>num2 and num4>num3 and num4>num1):
    print("Num4 is the Greatest Number:", num4)