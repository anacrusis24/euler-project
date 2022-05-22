'''
---------- test_euler_11_20.py ----------
Time    :  2022/05/22 09:14:46
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  The unit tests for Euler problems 11 - 20
'''


##### Imports #####
import pytest
import os
import sys

# Append path to see euler problems
path = os.path.abspath('.\\euler_problem')
sys.path.append(path)

from euler_problem_11_20 import *


##### Euler Tests #####
def test_euler_11():
    max_prod = greatest_product(2)
    assert max_prod == 9603

def test_euler_12():
    tri_num = tri_num_divisor(5)
    assert tri_num == 28

def test_euler_13():
    first_10_digit = first_n_digits_sum(10)
    assert first_10_digit == '5537376230'

def test_euler_14():
    long_chain_num = longest_collatz_chain(5)
    assert long_chain_num == 3

def test_euler_15():
    paths = lattice_paths(2, 2)
    assert paths == 6
    
##### My Tests #####
def test_collatz_sequence():
    sequence = collatz_sequence(13)
    assert sequence == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]