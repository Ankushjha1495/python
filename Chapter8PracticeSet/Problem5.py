def Pattern(n):
    if(n==0):
        return 0
    print("*"*n)
    Pattern(n-1)
Pattern(3)        