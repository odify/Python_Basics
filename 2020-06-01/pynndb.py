from numpy import exp, array, random, dot

class neural_network:
    def __init__(self):
        random.seed(1)
        self.weights = 3 * random.random((3, 1)) - 1
        
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))



    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = dot(inputs.T, error * output*(1-output))
            self.weights += adjustment



    def think(self, inputs):
        result = self.__sigmoid(dot(inputs, self.weights))
        return result

network = neural_network()

# TRAININGSET:

inputs = array([[1, 1, 1], [1, 0, 1], [0, 1, 1]])
outputs = array([[1, 1, 0]]).T

# USE TRAININGSET:

network.train(inputs, outputs, 10000)

#NEURALNETWORK OUTPUT:

print(network.think(array([1, 0, 0])))

#END