 #score
score = 0 
#start screen
play=input("want to play this super awesome amazing quiz?")



  #number of attempts
while True:
    try:
      tries = int(input("how many attempts do you want per question? 1-5"))
      tries = int(tries)
      break
    except:
      print("thats not a number")
    
while play== "yes":  
    #Ask name and save it
    name=input("what is your name?")

    #greet the user to the quiz
    print("hello",name, "welcome to this quiz lets get started!")
    question_attempts = tries
    while question_attempts > 0:
      #ask question
      awnser=input("where is the eifell tower?").lower()

      #check if awnser is correct then give feedback
      if awnser == "france".lower():
        print("correct you aren't an idiot")
        score += 5
        print("Your score is now",score)
      elif awnser == "":
        print("I'm not gonna give you the awnser give me an actual awnser")
      else:
        print("no you idiot! its france! YOUR SCORE IS STILL", score)

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
        print("good jon! your score is now", score)
        score += 5
      elif awnser == "":
        print("wow I guess you don't want a point then")

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
        print("yes congrats that was hard wasn't it heres 2 points!") 
        score += 2

      else:
        print("nuh uh")
        score -=9999999999999999999999999
      
      #end quiz
      print("congrats {}, completed the quiz!! you have a grand total score of {}".format(name, score) )
      play = input("wish to play again?").lower()

      print("thanks for playing")
      break