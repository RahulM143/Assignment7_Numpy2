#Problem Statement
#Write a function to find moving average in an array over a window:
#Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.

import numpy as np

lis = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
k = 3 # window of 3
n = len (lis) # elements in the list
ele = n - k + 1 # elements in moving avg sequence
ele
arr = np.array(lis)
arr

def movavg(array,elements): # defined function for moving average
    s = 0
    c = 0
    for i in array:
       r = np.average(array[s:s+3])
       s+=1
       c+=1
       print ('Y'+str(c),' '*c, r)
       if c ==elements:
           break

print ('\nThe moving avg sequence for the given array')
print ('-'*45)
dis = movavg(arr,ele)




