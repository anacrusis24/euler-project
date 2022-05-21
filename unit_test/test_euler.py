'''
---------- test_euler.py ----------
Time    :  2022/05/21 12:49:51
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  The unit tests for Euler problems
'''
''

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

def test_euler_7():
    n_prime = nth_prime(6)
    assert n_prime == 13

def test_euler_8():
    product = n_product(4)
    assert product == 5832

def test_euler_9():
    pyth_trip_prod = pyth_prod_triplet(12)
    assert pyth_trip_prod == 60

def test_euler_10():
    prime_sum = sum_prime(10)
    assert prime_sum == 17

##### My Tests #####
def test_prime_factors():
    pri_factors = prime_factors(2520)
    arr = np.array([2, 2, 2, 3, 3, 5, 7])
    assert (pri_factors == arr).all()

def test_list_primes():
    primes = list_primes(100)
    arr = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
                    dtype=int)
    assert (primes == arr).all()

def test_nth_prime():
    n_prime = nth_prime(1)
    assert n_prime == 2

def test_nth_prime_exceed():
    n_prime = nth_prime(80000)
    assert n_prime == 1020379

def test_pyth_prod_triplet():
    pyth_trip_prod = pyth_prod_triplet(40)
    assert pyth_trip_prod == 2040

def test_find_factor_pairs():
    pairs = find_factor_pairs(18)
    assert pairs == [[1, 18], [2, 9], [3, 6]]