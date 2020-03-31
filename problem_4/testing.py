#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: libby
"""

from problem4 import *

def main():
    
    print("Test 0: n = 0")
    answer0 = num_1s(0)
    print("Actual Result:", answer0)
    print("Expected Result:", 0)
    assert(answer0 == 0)
    print()
        
    print("Test 1: n = 1")
    answer1 = num_1s(1)
    print("Actual Result:", answer1)
    print("Expected Result:", 1)
    assert(answer1 == 1)
    print()
    
    print("Test 2: n = 17")
    answer2 = num_1s(17)
    print("Actual Result:", answer2)
    print("Expected Result:", 10)
    assert(answer2 == 10)
    print()
    
    print("Test 3: n = 15")
    answer3 = num_1s(15)
    print("Actual Result:", answer3)
    print("Expected Result:", 8)
    assert(answer3 == 8)
    print()
    
    print("Test 4: n = -1")
    answer4 = num_1s(-1)
    print("Actual Result:", answer4)
    print("Expected Result:", 0)
    assert(answer4 == 0)
    print()
    
    print("Test 5: n = 103")    
    answer5 = num_1s(103)
    print("Actual Result:", answer5)
    print("Expected Result:", 25)
    assert(answer5 == 25)
    print()
    
    print("Test 6: n = -103")
    answer6 = num_1s(-103)
    print("Actual Result:", answer6)
    print("Expected Result:", 0)
    assert(answer6 == 0)
    print()
    
    print("Test 7: n = 11")
    answer7 = num_1s(11)
    print("Actual Result:", answer7)
    print("Expected Result:", 4)
    assert(answer7 == 4)
    print()
    
    print("Test 8: n = 10")
    answer8 = num_1s(10)
    print("Actual Result:", answer8)
    print("Expected Result:", 2)
    assert(answer8 == 2)
    print()
    
    print("Test 9: n = 91")
    answer9 = num_1s(91)
    print("Actual Result:", answer9)
    print("Expected Result:", 20)
    assert(answer9 == 20)
    print()
    
    print("Test 10: n = 111")
    answer10 = num_1s(111)
    print("Actual Result:", answer10)
    print("Expected Result:", 36)
    assert(answer10 == 36)

if __name__ == '__main__':
    main()


