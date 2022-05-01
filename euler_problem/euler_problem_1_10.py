'''
---------- euler_problem_1_10.py ----------
Time    :  2022/05/01 13:17:31
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  Function to solve Euler problems 1 - 10
'''


##### Imports #####
import numpy as np
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


def prime_factor(num):
    '''
    @prime_factor
    Function calculates the largest prime factor of the given number
    
    @Input
    num: the number to calculate largest prime factor

    @Output
    max_factor: the largest prime factor of the number
    '''
    # Initialize the current greatest factor, max possible factor, and list of numbers
    factors = np.array([])
    max_possible_factor = int(np.sqrt(num))
    num_list = np.arange(0, max_possible_factor + 1, 1)

    # Run the loop to find the greatest prime factor
    for i in range(2, max_possible_factor):
        if num_list[i] != 0:
            # Set all the multiples of the lowest prime factor to 0
            num_list[num_list[i::i]] = 0
            num_list[i] = i

            # If it was a prime factor
            if num % i == 0:
                # Add it to the list
                factors = np.append(factors, num_list[i])
    
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