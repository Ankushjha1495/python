#This code will check if the list items are starting with the letter A or not
#and if yes it will say Hello "Name"
s = ["Ankush", "Angad", "Kai", "Kivi"]
for name in s:
    if(name.startswith("A")):
        print(f"Hello {name}")