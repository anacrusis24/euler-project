'''
---------- euler_problem_1_10.py ----------
Time    :  2022/05/01 12:00:59
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  Function to solve Euler problems 1 - 10
'''
'2022/05/01 02:28:36'

##### Imports #####
import numpy as np


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