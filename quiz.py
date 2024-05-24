#list of questions
QUESTION_FORMAT="{}\nA.{} B.{} C.{}"
QUESTIONS = ["where is the eiffel tower?",
    "where is france?",
    "where is the UK?"]
OPTIONS = [["France","America","Paris"],
            ["around paris", "inside europe", "between germany and spain"],
             ["next to water", "next to france", "next to ireland"]]
SHORT_OPTOINS = ["a", "b", "c", "d"]
AWNSERS = [0,0,0]

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
#start of quiz    
while play == "yes".lower():  
    #Ask name and save it
    name=input("what is your name?")

    #greet the user to the quiz
    print("hello",name, "welcome to this quiz lets get started!")

    #doing number of attempts per question
    for x in range(len(QUESTIONS)):
      question_attempts = tries
      while question_attempts > 0:
      
        #ask user a question
        awnser = input(QUESTION_FORMAT.format(QUESTIONS[x], OPTIONS[x][0],
                                              OPTIONS[x][1], OPTIONS[x][2],)).lower()
        #checks if user got question right
        if awnser == OPTIONS [x][AWNSERS[x]].lower() or awnser == SHORT_OPTOINS [AWNSERS[x]].lower():
          print(random.choice(GOOD_COMMENTS)) 
          score=+5
          break
        elif awnser == "":
          print("indecisive peasant")
        elif awnser in SHORT_OPTOINS or awnser in OPTIONS[x]:
          print(random.choice(BAD_COMMENTS))
        else:
          print("that wasn't an option")


          question_attempts -= 1
      
       
      
  #end quiz
    print("congrats {}, completed the quiz!! you have a grand total score of {}".format(name, score) )
    play = input("wish to play again?").lower()
    if play == "yes".lower():
      print("ok")
    else:
      print("thanks for playing")
      break