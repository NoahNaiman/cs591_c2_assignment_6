#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: libby
"""

#I left in the different iterations that this function took on to show how I 
#built up the function using TDD

#Start: No functions. Test failed.

#Iteration 1: Only 0 test passed.
'''def num_1s(n):
    """
    takes in some integer n and returns the total number of times the digit 1 
    appears in all non-negative integers that are less than or equal to n
    """
        return 0
'''

#Iteration 2: Only 0 test and 1 test
'''def num_1s(n):
    """
    takes in some integer n and returns the total number of times the digit 1 
    appears in all non-negative integers that are less than or equal to n
    """
        if n == 0:
            return 0
        else:
            return 1
'''

#Iteration 3: Only 0 test, 1 test, and 17 test
''' def num_1s(n):
    """
    takes in some integer n and returns the total number of times the digit 1 
    appears in all non-negative integers that are less than or equal to n
    """
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return 10
'''

#Iteration 4: Only 0 test, 1 test, 17 test, and 15 test. Failed for negative ints.
''' def num_1s(n):
    """
    takes in some integer n and returns the total number of times the digit 1 
    appears in all non-negative integers that are less than or equal to n
    """
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            nums_with_1s = [sum([1 for y in str(x) if y == '1']) for x in range(n+1)]
            return sum(nums_with_1s)
            
'''

#Iteration 5: 0 test, 1, test, 17 test, 15 test, -1 test. 
def num_1s(n):
    """
    takes in some integer n and returns the total number of times the digit 1 
    appears in all non-negative integers that are less than or equal to n
    """
    #If n is neg. or 0, return 0 as there are no numbers that fit the qualifications
    if n <= 0:
        return 0
    #If n is 1, return 1 as itself is the only number that fits the qualifications
    if n == 1:
        return 1
    #Otherwise, count up how many 1s are in each number in the range 0 to n (inclusive)
    #Then, total all of those counts
    else:
        nums_with_1s = [sum([1 for y in str(x) if y == '1']) for x in range(n+1)]
        return sum(nums_with_1s)
    
#After this, added tests for 103, -103, 11, 10, 91, 111 and all still passed
#Felt comfortable in the logic that got me to this point and included a variety
#of different tests that made the work confident enough to leave the function as is

