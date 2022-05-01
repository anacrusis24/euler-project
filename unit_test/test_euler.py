'''
---------- test_euler.py ----------
Time    :  2022/05/01 13:17:31
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  The unit tests for Euler problems
'''

##### Imports #####
import pytest
import os
import sys

# Append path to see euler problems
path = os.path.abspath('.')
sys.path.append(path)

from euler_problem.euler_problem_1_10 import *


##### Unit Tests #####
def test_euler_1():
    sum_mult_3_5 = sum_multiples([3, 5], 10)
    assert sum_mult_3_5 == 23

def test_euler_2():
    fib_sum = fibonacci_sum(100)
    assert fib_sum == 44

def test_euler_3():
    lrg_factor = prime_factor(13195)
    assert lrg_factor == 29

def test_euler_4():
    lrg_palindrome = palindrome(2)
    assert lrg_palindrome == 9009