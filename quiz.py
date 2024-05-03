#score
score = 0 
#Ask name and save it
name=input("what is your name?")
#greet the user to the quiz
print("hello" ,name, "welcome to this quiz lets get started!")
#ask question
awnser=input("where is the eifell tower?")
#check if awnser is correct then give feedback
if awnser == "france":
  print("correct you aren't an idiot")
  score += 5
  print("Your score is now",score)
elif awnser == "":
  print("I'm not gonna give you the awnser give me an actual awnser")
else:
  print("no you idiot! its france!")
#end quiz