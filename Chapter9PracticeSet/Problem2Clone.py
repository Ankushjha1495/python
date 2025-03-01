import random
def game():
    print("You are playing a game..")

    score = random.randint(1, 100)

    with open ("High-Score.txt")as f:
        highscore = f.read()
        if(highscore ==""):
            highscore =int(highscore)
        else:
            highscore =0

    print(f"Your Score is {score}")
    if(score>highscore):
        with open("High-Score.txt", "w") as f:
            f.write(str(score)) 
    return score
game()               

        
        