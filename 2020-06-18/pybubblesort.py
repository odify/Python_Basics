# BUBBLESORTING WITH PYTHON

import timeit

lst = [6,3,2,8,3,9,12]
print('1st Sorted List Technique\n')
print('Original:\n',lst,'\n')

def bubble_sort(x):
 while (all([x[i] <= x[i+1] for i in range(len(x)-1)])) != True:
  for i in range(len(x)-1):
   if x[i+1] < x[i]:
    x[i],x[i+1] = x[i+1],x[i]
 print('Bubblesort:\n',x,'\n')

func_time = timeit.default_timer()
bubble_sort(lst)

print('Time:\n',timeit.default_timer() - func_time)
print('\n','~'*38)
print('\n2nd Sorted List Technique\n')


import timeit

lst1 = [6,3,2,8,3,9,12]
print('Original:\n',lst1,'\n')

def bubble_sort(x):
 for a in range(len(x)-1):
  for i in range(len(x)-1):
   if x[i+1] < x[i]:
    x.insert(i,(x.pop(i+1)))    
 print('Bubblesort:\n',x,'\n')

func_time = timeit.default_timer()
bubble_sort(lst1)

# print('Time:\n',timeit.default_timer() - func_time)