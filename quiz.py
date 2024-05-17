#list of questions
QUESTIONS = [
    "where is the eiffel tower?",
    "where is france?",
    "where is the UK?"]
OPTIONS = [["france",
            "around paris",
            "next to water", "next to france", "next to ireland"]]
SHORT_OPTOINS = ["a", "b", "c", "d"]
AWNSERS = [1, 1, 1]

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
        
        #ask question
        awnser=input("where is the eifell tower?").lower()
        
        #check if awnser is correct then give feedback
        if awnser == "france".lower():
          score += 5
          print(random.choice(GOOD_COMMENTS))
          print("Your score is now",score)
          break
        elif awnser == "":
          print("I'm not gonna give you the awnser give me an actual awnser")
        else:
          print(random.choice(BAD_COMMENTS))
          print("YOUR SCORE IS STILL", score)
        question_attempts -= 1
        
    #2nd question intro
    are_you_ready=input ("ready for the next question?")
    if are_you_ready == "yes":
        print("good here we go")
    else:
        print("oh well gosh diddly darn too bad")

      #ask 2nd question
    awnser=input ("where is france?").lower()
      #check if awnser is correct then give feedback
    if awnser == "around paris".lower():
        (random.choice(GOOD_COMMENTS))
        score += 5
        
    elif awnser == "":
          print("wow I guess you don't want a point then")
          
    else:
          print(random.choice(BAD_COMMENTS))
          print("YOUR SCORE IS STILL", score)
          question_attempts -= 1

          

      #3rd question multiple choice intro
    are_you_ready=input ("ready for the next question?")
    if are_you_ready == "yes":
        print("good here we go")
    else:
        print("oh well gosh diddly darn too bad")

      #3rd question multiple choice 
    question = "where is the UK?"
    a = "next to france"
    b = "next to water"
    c = "next to ireland"
    answer = input("{}\nA.{} B.{} C.{}".format(question, a, b, c)).lower()

      #3rd question multiple choice awnser
    if answer == b or answer == "b":
        print(random.choice(GOOD_COMMENTS))
        score += 2

    else:
        print("nuh uh")
        score -=99999999999999
      
      #end quiz
    print("congrats {}, completed the quiz!! you have a grand total score of {}".format(name, score) )
    play = input("wish to play again?").lower()

    print("thanks for playing")
    break