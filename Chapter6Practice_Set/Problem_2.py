#This code tells that if you are failed or passed the conditions are
#if marks of any subjects are less than 33 than you are failed and
#if total marks percentage is less than 40 than you are also failed 
#else you are pass
marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))
marks3 = int(input("Enter marks 3:"))
# check for total percentage
total_percentage = (100)*(marks1+marks2+marks3)/300
if(total_percentage>40 and marks1>33 and marks2>33 and marks3>33):
    print("Congratulations, You are Pass", total_percentage)

else:
    print("You are failed!")