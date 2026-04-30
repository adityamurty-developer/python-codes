import random

def game():
    print("You are playing a game....")
    score = random.randint(1, 50)

    with open("hiscore.txt") as f:
        hi_score = f.read()
        if(hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0

    print(f"Your score is: {score}")

    if(score > hi_score):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()