import random

def game():
    print("You are playing a game... ")

    score = random.randint(1,70)

    #Fetch the Highscore
    with open("High-Score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore =int(hiscore)
        else:
            hiscore = 0

    print(f"Your Score: {score}")

    if(score>hiscore):
        with open("High-Score.txt", "w") as f:
            f.write(str(score))

    return score

game()                  










