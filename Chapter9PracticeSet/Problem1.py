f = open("poem1.txt")
read = f.read()
if ("Twinkle" in read):
    print("The word twinkle is present Here")
else:
    print("The word Twinkle is Not present here")    

f.close()