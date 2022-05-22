'''
---------- test_euler_11_20.py ----------
Time    :  2022/05/21 17:49:11
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  None
'''


##### Imports #####
import pytest
import os
import sys

# Append path to see euler problems
path = os.path.abspath('.')
sys.path.append(path)

from euler_problem.euler_problem_11_20 import *


##### Euler Tests #####
def test_euler_11():
    max_prod = greatest_product(2)
    assert max_prod == 9306