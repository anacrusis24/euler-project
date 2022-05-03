'''
---------- test_euler.py ----------
Time    :  2022/05/02 21:00:09
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


##### Euler Tests #####
def test_euler_1():
    sum_mult_3_5 = sum_multiples([3, 5], 10)
    assert sum_mult_3_5 == 23

def test_euler_2():
    fib_sum = fibonacci_sum(100)
    assert fib_sum == 44

def test_euler_3():
    lrg_factor = greatest_prime_factor(13195)
    assert lrg_factor == 29

def test_euler_4():
    lrg_palindrome = palindrome(2)
    assert lrg_palindrome == 9009

def test_euler_5():
    sml_mult = smallest_multiple(10)
    assert sml_mult == 2520

def test_euler_6():
    diff = sqr_sum_sqr(10)
    assert diff == 2640

##### My Tests #####
def test_prime_factors():
    pri_factors = prime_factors(2520)
    arr = np.array([2, 2, 2, 3, 3, 5, 7])
    assert (pri_factors == arr).all()