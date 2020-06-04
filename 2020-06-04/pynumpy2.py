#UNDER CONSTRUCTION...

def part(x):
   print ("Part {a}:\n".format(a = x))
def line():
    print("_"*38)

import random
import numpy
a = [0,30,60,90]
chance = [0.90,0.05,0.04,0.01] # *sum must be equal to 1 ( 0.9+0.05+0.04+0.01=1 )

result = numpy.random.choice(a ,p = chance)
print(result)