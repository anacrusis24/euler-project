'''
---------- main.py ----------
Time    :  2022/05/23 19:44:15
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  The main program to see the answers to the Euler problems
'''

##### Imports #####
import os
import sys
path = os.path.abspath('.\\euler_problem')
sys.path.append(path)

import numpy as np
from euler_problem_1_10 import *
from euler_problem_11_20 import *
from display.display_problem import *
from exception.exception import *


##### Main Program #####
if __name__ == '__main__':
    # Global variables we need for display
    num_problems = 18
    problem_prompt = 'Enter which Euler problem you would like to solve: '
    solve_prompt = 'Would you like to solve more problems (y/n): '

    # Loop to continue solving Euler problems
    continue_solving = True
    while continue_solving:

        # Get the problem to solve 
        while True:
            try:
                # Get the problem from the user
                problem_to_solve = int(input(problem_prompt))

                # Raise an exception if not an integer
                if not isinstance(problem_to_solve, int):
                    raise NotAnInteger
                # Raise an exception if not in range
                elif problem_to_solve > num_problems:
                    raise NotInRange
                else:
                    problem_header = f'---------- Euler Problem {problem_to_solve} ----------'
                    break
            except ValueError:
                print('Only enter integer values. Ex. 1, 2, 3,...')
            except NotInRange:
                print(f'Enter only integers from 1 to {num_problems}')

        
        ### Euler Problem 1 ###
        if problem_to_solve == 1:
            sum_mult_3_5 = sum_multiples(np.array([3, 5]), 1000)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_1.txt', problem_to_solve, sum_mult_3_5)
        
        ### Euler Problem 2 ###
        elif problem_to_solve == 2:
            fib_sum = fibonacci_sum(4000000)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_2.txt', problem_to_solve, fib_sum)

        ### Euler Problem 3 ###
        elif problem_to_solve == 3:
            lrg_factor = greatest_prime_factor(600851475143)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_3.txt', problem_to_solve, lrg_factor)
        
        ### Euler Problem 4 ###
        elif problem_to_solve == 4:
            lrg_palindrome = palindrome(3)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_4.txt', problem_to_solve, lrg_palindrome)

        ### Euler Problem 5 ###
        elif problem_to_solve == 5:
            sml_mult = smallest_multiple(20)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_5.txt', problem_to_solve, sml_mult)

        ### Euler Problem 6 ###
        elif problem_to_solve == 6:
            diff = sqr_sum_sqr(100)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_6.txt', problem_to_solve, diff)

        ### Euler Problem 7 ###
        elif problem_to_solve == 7:
            nth_prime = nth_prime(10001)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_7.txt', problem_to_solve, nth_prime)
        
        ### Euler Problem 8 ###
        elif problem_to_solve == 8:
            product = n_product(13)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_8.txt', problem_to_solve, product)

        ### Euler Problem 9 ###
        elif problem_to_solve == 9:
            pyth_trip_prod = pyth_prod_triplet(1000)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_9.txt', problem_to_solve, pyth_trip_prod)

        ### Euler Problem 10 ###
        elif problem_to_solve == 10:
            prime_sum = sum_prime(2000000)
            display_results(problem_header, 'display/problem_statements_1_10/problem_statement_10.txt', problem_to_solve, prime_sum)

        ### Euler Problem 11 ###
        elif problem_to_solve == 11:
            max_prod = greatest_product(4)
            display_results(problem_header, 'display/problem_statements_11_20/problem_statement_11.txt', problem_to_solve, max_prod)

        ### Euler Problem 12 ###
        elif problem_to_solve == 12:
            tri_num = tri_num_divisor(500)
            display_results(problem_header, 'display/problem_statements_11_20/problem_statement_12.txt', problem_to_solve, tri_num)

        ### Euler Problem 13 ###
        elif problem_to_solve == 13:
            n_digits = first_n_digits_sum(10)
            display_results(problem_header, 'display/problem_statements_11_20/problem_statement_13.txt', problem_to_solve, n_digits)

        ### Euler Problem 14 ###
        elif problem_to_solve == 14:
            long_chain_num = longest_collatz_chain(1000000)
            display_results(problem_header, 'display/problem_statements_11_20/problem_statement_14.txt', problem_to_solve, long_chain_num)

        ### Euler Problem 15 ###
        elif problem_to_solve == 15:
            paths = lattice_paths(20, 20)
            display_results(problem_header, 'display/problem_statements_11_20/problem_statement_15.txt', problem_to_solve, paths)

        ### Euler Problem 16 ###
        elif problem_to_solve == 16:
            pwd_sum = power_digit_sum(1000)
            display_results(problem_header, 'display/problem_statements_11_20/problem_statement_16.txt', problem_to_solve, pwd_sum)

        ### Euler Problem 17 ###
        elif problem_to_solve == 17:
            letter_count = number_letter_count(1000)
            display_results(problem_header, 'display/problem_statements_11_20/problem_statement_17.txt', problem_to_solve, letter_count)

        ### Euler Problem 18 ###
        elif problem_to_solve == 18:
            path_sum = max_path_sum()
            display_results(problem_header, 'display/problem_statements_11_20/problem_statement_18.txt', problem_to_solve, path_sum)

        # Let user decide weather to keep solving or not 
        while True:
            try:
                # Collect user answer
                solve_answer = input(solve_prompt)

                # Raise an exception if not 'y' or 'n'
                if solve_answer not in ['y', 'n']:
                    raise NotYesNo
                else:
                    break
            except NotYesNo:
                print('Enter only \'y\' or \'n\'')

        # End solving session 
        if solve_answer == 'n':
            continue_solving = False