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

# ----- MAIN CODE ----- 

intro()

tries = getNunber()
