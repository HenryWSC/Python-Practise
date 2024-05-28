guesses =[]
MOST_DOWNLOADED_GAMES_AWNSERS = ["subway surfers", "stumble guys", "roblox", "condy crush saga", "race master 3d", "8 ball pool", "fifa mobile", "merge and fight", "garena free fire", "bridge race"]
import random

score = 0
MAX_TURNS = 10

# ----- FUNCTIONS -----

def intro():
    print("hello world")
    #Ask name and save it
    name=input("what is your name?")

    #greet the user to the quiz
    print("hello",name, "welcome to this quiz lets get started!")
    print("this quiz is about the top 10 best numbers.")

def getPassword():
    while True:
        password = input("whats the password?")
        if password == "trogdor":
            return
        else:
            print("nope. Try again.")
def getNunber():
    number = input ("give me a number")
    return int(number)

number = getNunber()
print(number)

def getLives():
    while True:
        lives = input("how many cances do you want?")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("please choose a positive number")
        except:
            print("that wasn't a number")

def isCorrect(answer, list):
    if awnser in list:
        return True
    else:
        return False
    
if inList(answer, MOST_DOWNLOADED_GAMES_AWNSERS):
    if inList(answer,guesses):
        print("you have already guessed that")
    else:
        print("correct")
        score += 5
        guesses.append(answer)

# ----- MAIN CODE -----
lives = getLives()
score = 0
intro()


while lives > 0:
    awnser = input("what is one of the top 10 most popular games in 2023\n").lower() 

    if isCorrect(awnser, MOST_DOWNLOADED_GAMES_AWNSERS) == True:
        print("Correct!")
        score +=5
    else:
        print("wrong")
        lives -= 1

print("game Over. your final score was {}".format(score))


