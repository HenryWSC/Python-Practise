guesses =[]
MOST_DOWNLOADED_GAMES_AWNSERS = ["subway surfers", "stumble guys", "roblox", "condy crush saga", "race master 3d", "8 ball pool", "fifa mobile", "merge and fight", "garena free fire", "bridge race"]
import random

score = 0
MAX_TURNS = 10

# ----- FUNCTIONS -----

def intro():
    #Ask name and save it
    name=input("what is your name?")

    #greet the user to the quiz
    print("hello",name, "welcome to this quiz lets get started!")
    print("this quiz is about the top 10 best numbers.")

def getLives():
    while True:
        lives = input("how many chances do you want?")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("please choose a positive number")
        except:
            print("that wasn't a number")

def inList(answer, list):
    if answer in list:
        return True
    else:
        return False
    

# ----- MAIN CODE -----
intro()
lives = getLives()
score = 0

while lives > 0:
    answer = input("what are the top 10 most downloaded games")
    if inList(answer,MOST_DOWNLOADED_GAMES_AWNSERS):
        if inList(answer, guesses):
            print("you have already guessed that")
        else:
            print("correct")
            score += 5
            guesses.append(answer)
            print("you have already guessed {}. your score is {}. you have {} chances remaining".format(len(guesses), score, lives))
    else:
        print("wrong")
        lives -= 1
        print("you have already guessed {}. Your score is {}. You have {} chances left".format(len(guesses), score, lives))


print("game Over. your final score was {}".format(score))


