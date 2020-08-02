#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
count = 0                            # attempts counter
number = np.random.randint(1,101)    # generates random integer between 1 and 101
print ("Guess the number from 1 to 100")

def game_core_v3(number):
    '''Creating function for binary search. 
    The function accepts a number and returns a number of attempts.'''
    digit_list = [digit for digit in range (1, 101)] #Creating a list of 100 elements
    low = digit_list[0] #defining smallest element in a list
    high = digit_list[-1] #defining largest list element
    count = 0
    
    while low <= high: #loop until the smallest and largest list elements match
        count+=1
        mid = (low+high) // 2 # middle element of the list
        
        if mid > number:
            high = mid-1 #if number is less than middle element of a list, define middle element as the upper border
        elif mid < number:
            low = mid+1  #if number is more than middle element of a list, define middle element as the lower border
        else:
            break # exit the loop
    
    return(count)

print ("You guessed the number {} in {} attempts.".format(number, game_core_v3(count)))


# In[ ]:




