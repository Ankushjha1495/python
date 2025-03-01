#Here we are making a function to remove some words from the give
#List we used a for loop for this 

def remove(list, word):      #Remove is the function name, "list" and "word" are the two parameters
    for items in list:       # This will iterate all the list values
        list.remove(word)    #This remove function will remove a certain words from the list
        return list              #this will return our list
Oceans = ["Pacific Ocean", "Indian Ocean", "Arctic Ocean"]
print(remove(Oceans, "Indian Ocean"))    
    