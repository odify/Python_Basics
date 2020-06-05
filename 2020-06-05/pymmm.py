#mean()method
import numpy

speed = [31,115,118,22,55,27,17,78,77,82,81]

x = numpy.mean(speed)

print(x)
#---------------------------------------------------
#median()method
import numpy

speed = [31,115,118,22,55,27,17,78,77,82,81]

x = numpy.median(speed)

print(x)
#---------------------------------------------------
import numpy

speed = [31,115,118,22,55,27,17,78,77,82,81]

x = numpy.median(speed)

print(x)
#---------------------------------------------------
#SciPy mode()

from scipy import stats

speed = [31,115,118,22,55,27,17,78,77,82,81]

x = stats.mode(speed)

print(x)
#---------------------------------------------------
# WICHTIG: 
# Mean - Der Durchschnittswert
# Median - Der Mittelwert/Mittelpunkt
# Mode - Häufigster Wert