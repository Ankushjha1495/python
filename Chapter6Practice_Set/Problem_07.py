#This code will lower the "Ankush" and also Your Post too and will check if the 
#Post is talking about Ankush or not
Post = input("Enter the Post:")

if("Ankush".lower() in Post.lower()):
    print("The post is Talking About Ankush");
else :
    print("The post is not talking about Ankush");