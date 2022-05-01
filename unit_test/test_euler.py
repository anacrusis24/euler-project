'''
---------- test_euler.py ----------
Time    :  2022/04/30 21:10:46
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  The unit tests for Euler problems
'''

##### Imports #####
import pytest
import numpy as np
import os
import sys

# Append path to see euler problems
path = os.path.abspath('.')
sys.path.append(path)

from euler_problem.euler_problem_1_10 import *

##### Unit Tests #####
def test_euler_1():
    sum_mult_3_5 = sum_multiples(np.array([3, 5]), 10)
    assert sum_mult_3_5 == 23
        
