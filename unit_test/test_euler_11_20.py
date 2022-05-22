'''
---------- test_euler_11_20.py ----------
Time    :  2022/05/21 17:49:11
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

##### My Tests #####