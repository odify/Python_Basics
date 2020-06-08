# import random
# import sys

# options = {1:"rock",2:"scissor",3:"paper"}
# results = {0:"Draw",1:"You win",2:"Computer wins"}

# try:
#     user_input = int(input("Enter your choice (1=rock, 2=scissor, 3=paper)\n"))
# except ValueError:
#     print("Please enter 1, 2 or 3")
#     sys.exit()
    
    
# computer = random.randint(1,3)


# print(" Computer : "+options[computer])
# print(" You : "+options[user_input])



# result=(computer-user_input+3)%3
# print("Result is: "+results[result])


# NEW VERSION // lambda way...

from random import randint

def game():
  p1 = randint(1,3)
  p2 = randint(1,3)
  if p1 == p2:
    result = 0
  elif p1 == p2+1 or p1 == p2-2:
    result = 1
  else:
    result = 2
  return [p1, p2, result]
  
def percent(k):
  return str(round(k/n*100))+"%"


games =[]
n = 10000
for i in range(n):
  games.append(game())
  
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
modes = ["Picks:", "Wins:", "Draws:", "Losses:"]
p = len(games)
w = len(list(filter(lambda x: x[2] == 1, games)))
d = len(list(filter(lambda x: x[2] == 0, games)))
l = p-w-d
statsp1 = {"Picks:": p, "Wins:": w, "Draws:": d, "Losses:": l}
statsp2 = {"Picks:": p, "Wins:": l, "Draws:": d, "Losses:": w}

print("            Player 1         Player2")
for m in modes:
  print("{:8s}".format(m), "{:7d}".format(statsp1[m]), "{:7s}".format(percent(statsp1[m])), "{:7d}".format(statsp2[m]), "{:7s}".format(percent(statsp2[m])))
  for k,v in choices.items(): 
    a = list(filter(lambda x: x[0] == k, games))
    b = list(filter(lambda x: x[1] == k, games))
    if m == "Picks:":
      print("{:8s}".format(v), "{:7d}".format(len(a)), "{:7s}".format(percent(len(a))), "{:7d}".format(len(b)), "{:7s}".format(percent(len(b))))
    elif m == "Wins:":
      c = list(filter(lambda x: x[2] == 1, a))
      e = list(filter(lambda x: x[2] == 2, b))
      print("{:8s}".format(v), "{:7d}".format(len(c)), "{:7s}".format(percent(len(c))), "{:7d}".format(len(e)), "{:7s}".format(percent(len(e))))
    elif m == "Losses:":
      c = list(filter(lambda x: x[2] == 2, a))
      e = list(filter(lambda x: x[2] == 1, b))
      print("{:8s}".format(v), "{:7d}".format(len(c)), "{:7s}".format(percent(len(c))), "{:7d}".format(len(e)), "{:7s}".format(percent(len(e))))
    else:
      c = list(filter(lambda x: x[2] == 0, a))
      e = list(filter(lambda x: x[2] == 0, b))
      print("{:8s}".format(v), "{:7d}".format(len(c)), "{:7s}".format(percent(len(c))), "{:7d}".format(len(e)), "{:7s}".format(percent(len(e)))) 
  print()