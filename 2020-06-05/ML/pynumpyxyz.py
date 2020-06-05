# Variance...
import numpy

speed = [31,115,118,22,55,27,17]

x = numpy.var(speed)

print(x)

#Standart deviation:

import numpy

speed = [31,115,118,22,55,27,17]

x = numpy.std(speed)

print(x)

# percentile() method

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print(x)