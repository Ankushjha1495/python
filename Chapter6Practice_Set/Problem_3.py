#This code is to remove the spam comment, if p1,p2,p3,p4 exists in the message
#Then the code will tell that the comment is a spam
P1 = "Make a lot of money"
P2 = "buy now"
P3 = "Subscribe this"
P4 = "Click this"
Message = input("Enter your comment here")

if((P1 in Message) or (P2 in Message) or (P3 in Message) or (P4 in Message)):
    print("Your Comment is a Spam")

else:
    print(Message)    