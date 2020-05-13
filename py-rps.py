import random
import sys

options = {1:"rock",2:"scissor",3:"paper"}
results = {0:"Draw",1:"You win",2:"Computer wins"}

try:
    user_input = int(input("Enter your choice (1=rock, 2=scissor, 3=paper)\n"))
except ValueError:
    print("Please enter 1, 2 or 3")
    sys.exit()
    
    
computer = random.randint(1,3)


print(" Computer : "+options[computer])
print(" You : "+options[user_input])



result=(computer-user_input+3)%3
print("Result is: "+results[result])