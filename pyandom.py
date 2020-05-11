import random

a =[]

n = int(input("enter number of elemets: \n"))
for j in range(n):
    a.append(random.randint(1,100))
    
print('Random no. list is: ',a)
