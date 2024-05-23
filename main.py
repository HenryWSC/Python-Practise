#list of questions
QUESTION_FORMAT="{}\nA.{} B.{} C.{}"
QUESTIONS = ["where is the eiffel tower?",
    "where is france?",
    "where is the UK?"]
OPTIONS = [["France","America","Paris"],
            ["around paris", "next to water", "next to france", "next to ireland"]]
SHORT_OPTOINS = ["a", "b", "c", "d"]
AWNSERS = [0,0]

#comments
import random
GOOD_COMMENTS = ["you aren't retarted!", "your not a doofus", "you aren't dumb", "you might be barely passable as smart"] 
BAD_COMMENTS = ["your IQ is room tempurature", "your retarted", "congrats a doofus is you!"]

#score
score = 0 

#start screen
play=input("want to play this super awesome amazing quiz?")



  #number of attempts
while True:
    try:
        tries = input("how many attempts do you want per question? 1-5")
        tries = int(tries)
        break
    except:
      print("thats not a number")
    
while play== "yes":  
    #Ask name and save it
    name=input("what is your name?")

    #greet the user to the quiz
    print("hello",name, "welcome to this quiz lets get started!")

    #doing number of attempts per question
    question_attempts = tries
    while question_attempts > 0:
    
      #ask user a question
      awnser = input(QUESTION_FORMAT.format(QUESTIONS[0], OPTIONS[0][0],
                                            OPTIONS[0][1], OPTIONS[0][2],)).lower()
      if awnser == OPTIONS [0][AWNSERS[0]].lower() or awnser == SHORT_OPTOINS [AWNSERS[0]].lower():
        print(random.choice(GOOD_COMMENTS)) 
        score=+5
        break
      elif awnser in SHORT_OPTOINS or awnser in OPTIONS[0]:
        print(random.choice(BAD_COMMENTS))
      else:
        print("that wasn't an option")
      
       
      
    #end quiz
    print("congrats {}, completed the quiz!! you have a grand total score of {}".format(name, score) )
    play = input("wish to play again?").lower()

    print("thanks for playing")
    break