#Scatter Plot...

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(4.0, 1.0, 1000)
y = numpy.random.normal(8.0, 1.7, 1000)

plt.scatter(x, y)
plt.show()