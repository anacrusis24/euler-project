'''
---------- euler_problem_1_10.py ----------
Time    :  2022/05/02 21:00:09
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  Function to solve Euler problems 1 - 10
'''


##### Imports #####
import numpy as np
from collections import Counter
from tqdm import tqdm

##### Define Functions #####
def sum_multiples(multiples, max_num):
    '''
    @sum_multiples
    Function computes the sum of all the natural numbers which are below max_num and are multiples of a number in the multiples list
    
    @Input
    multiples: a list of natural numbers that are the base multiples 
    max_num: the max number (not inclusive) to calculate the sum
    
    @Output
    running_sum: the final sum of the multiples
    '''
    # initialize the running sum and starting number
    running_sum = 0
    n = 1

    # calculate the running sum
    while n < max_num:
        for mult in multiples:
            # if n is a multiple of one of the numbers in multiples
            if n % mult == 0:
                running_sum += n
                break

        n += 1
    
    return running_sum


def fibonacci_sum(max_num):
    '''
    @fibonacci_sum
    Function calculates the sum of all the even numbers less than the max number (not inclusive) 
    
    @Input
    max_num: the max number that we cannot exceed
    
    @Output
    fib_sum: the sum
    '''
    fib_sum = 2
    curr_fib = 2
    last_fib = 1

    while (curr_fib + last_fib) < max_num:
        # Calculate the next Fibonacci number
        next_fib = curr_fib + last_fib

        # Update the last and current fibonacci numbers
        last_fib = curr_fib
        curr_fib = next_fib
        
        if curr_fib % 2 == 0:
            fib_sum += next_fib
    
    return fib_sum


def prime_factors(num):
    '''
    @prime_factors
    Function calculates and returns the prime factors of the given number
    
    @Input
    num: the number to find the prime factors of
    
    @Output
    prime_factors: the list of prime factors
    '''
    # Initialize empty list for the prime factors
    prime_factors_arr = np.array([], dtype=int)

    # Find how many times 2 is a factor
    cur_num = num
    while cur_num % 2 == 0:
        prime_factors_arr = np.append(prime_factors_arr, 2)
        cur_num = cur_num / 2

    # Run the loop to find the non 2 prime factors
    i = 3
    while cur_num > 1:
        # If i is a prime factor
        if cur_num % i == 0:
            prime_factors_arr = np.append(prime_factors_arr, i)
            cur_num = cur_num / i
        else:
            i += 1

    return prime_factors_arr


def greatest_prime_factor(num):
    '''
    @prime_factor
    Function calculates the largest prime factor of the given number
    
    @Input
    num: the number to calculate largest prime factor

    @Output
    max_factor: the largest prime factor of the number
    '''
    # Initialize the current greatest factor, max possible factor, and list of numbers
    factors = prime_factors(num)
    
    # Fund the max factor
    max_factor = int(np.max(factors))

    return max_factor


def palindrome(n_digit):
    '''
    @palindrome
    Function calculates the largest palindrome made from the product of 2 n_digit numbers
    
    @Input
    n_digit: the number of digit numbers to be used in product

    @Output
    max_palindrome: the largest palindrome
    '''
    # Initialize list of palindromes
    palindromes = np.array([])
    
    # Get start and end numbers
    start_num = '1'
    end_num = '9'

    # Add the correct amount of 0s or 9s
    for i in range(1, n_digit):
        start_num += '0'
        end_num += '9'

    # Convert to int
    start_num = int(start_num)
    end_num = int(end_num)

    for i in tqdm(range(start_num, end_num + 1), desc='CALCULATING ANSWER'):
        for j in range(i, end_num + 1):
            # Calculate the product
            product = i * j

            # Check if palindrome
            is_palindrome = True
            str_product = str(product)
            len_str = len(str_product)
            max_indx = int(len_str / 2)

            for k in range(max_indx):
                if str_product[k] != str_product[len_str - 1 - k]:
                    is_palindrome = False
                    break

            # If product is a palindrome                
            if is_palindrome:
                palindromes = np.append(palindromes, product)

    # Find the max palindrome
    max_palindrome = int(np.max(palindromes))

    return max_palindrome


def smallest_multiple(max_num):
    '''
    @divisible_all
    Function finds the smallest number that is divisble by all integers up to the max_num (inclusive)
    
    @Input
    max_num: the max factor of the smallest number

    @Output
    min_num: the smalles number that is divisible
    '''
    # Initialize arrays
    cur_arr = np.array([])
    num_arr = np.arange(2, max_num + 1, 1)

    # Calculate how many of the prime factors to add
    for num in num_arr:
        # Calculate the prime factors
        prime_factors_arr = prime_factors(num)

        # Add the difference in prime factors to the list   
        diff = list((Counter(prime_factors_arr) - Counter(cur_arr)).elements())
        cur_arr = np.append(cur_arr, diff)

    # Calculate the minimum number
    min_num = int(np.prod(cur_arr))

    return min_num


def sqr_sum_sqr(max_num):
    '''
    @sqr_sum_sqr
    Function computes the difference between the square of the sums and the sum of squares of all natural numbers up to max_num
    
    @Input
    max_num: the maximum number to include in the sums
    
    @Output
    diff: the difference between the two values
    '''
    #Intialize values
    sum_sqr = 0
    sqr_sum = 0

    # Calculate the sum of square and square of sums
    for i in range(1, max_num + 1):
        sum_sqr += i**2
        sqr_sum += i
    
    sqr_sum = sqr_sum**2

    # Calculate the difference
    diff = sqr_sum - sum_sqr

    return diff