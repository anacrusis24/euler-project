'''
---------- euler_problem_1_10.py ----------
Time    :  2022/05/20 09:43:48
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


def list_primes(max_num):
    '''
    @list_primes
    Function lists all of the prime numbers beneath the max_num (inclusive)
    
    @Input
    max_num: the max possible prime
    
    @Output
    primes_list: the list of prime numbers
    '''
    # Create empty list of bools
    bool_list = np.ones(max_num, dtype=int)

    for i in range(2, int(np.sqrt(max_num)) + 1):
        if bool_list[i]:
            # Set the multiple to 0 but keep the original number
            bool_list[::i] = 0
            bool_list[i] = i

    primes_list = np.where(bool_list != 0)
    primes_list = np.delete(primes_list, 0)

    return primes_list


def nth_prime(n, max_num=1000000):
    '''
    @nth_prime
    Function returns the nth prime number (primes starting as 2, 3, 5, ...)
    
    @Input
    n: the prime number to find 
    
    @Output
    n_prime: the nth prime
    '''
    primes_list = list_primes(max_num)
    next_max = 10 * max_num

    if len(primes_list) >= n:
        n_prime = primes_list[n - 1]
    else:
        return nth_prime(n, max_num=next_max)    

    return n_prime


def n_product(n):
    '''
    @n_product
    Function finds the greatest product of n adjacent digits in the following number
    
    @Input
    n: the number of adjacent digits for the product
    
    @Output
    max_product: the greatest product of n adjacent digits
    '''
    str_num = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''

    # Make a new string to hold a single line number
    new_str = ''

    for line in str_num.splitlines():
        if line:
            new_str += line
    
    # Initialize empty product list and calculate the total number of permutations
    product_list = np.array([])
    num_products = len(new_str) - n

    for i in range(num_products + 1):
        # Get the substring to calculate the product
        sub_str = new_str[i:(n + i)]
        running_product = 1

        # Calculate the product of the substring
        for num in sub_str:
            int_num = int(num)
            running_product *= int_num

        # Append the product to the list
        product_list = np.append(product_list, running_product)

    # Get the max product
    max_product = int(np.max(product_list))

    return max_product


def find_factor_pairs(num):
    '''
    @find_factor_pairs
    Function finds all of the factor pairs for the given number
    
    @Input
    num: the number to find the factor pairs
    
    @Output
    factor_pairs: the factor pairs of the number
    '''
    # Create empty array to hold factor pairs
    factor_pairs = []

    # Generate the pairs
    for i in range(1, int(np.sqrt(num)) + 1):
        # If evenly divisible
        if num % i == 0:
            pair = [i, int(num/i)]
            factor_pairs.append(pair)

    return factor_pairs
    

def pyth_prod_triplet(sum_triplet):
    '''
    @pyth_prod_triplet
    Function finds the product of the Pythagorean triplet whose sum is sum_triplet
    
    @Input
    sum_triplet: the sum of the Pythagorean triplet
    
    @Output
    prod_triplet: the product of the Pythagorean triplet
    '''
    # Var to hold current triplet
    curr_triplet = np.array([0, 0, 0])
    r = 2
    
    # Generate triplets
    while (np.sum(curr_triplet) != sum_triplet) and (curr_triplet[0] <= sum_triplet):
        factors = find_factor_pairs(r**2/2)
        for pair in factors:
            # Find s and t
            s = pair[0]
            t = pair[1]

            # Find a, b, c
            a = r + s 
            b = r + t 
            c = r + s + t

            curr_triplet = np.array([a, b, c])

            if np.sum(curr_triplet) == sum_triplet:
                break
        
        r += 2

    # Find product of triplet
    prod_triplet =  int(np.prod(curr_triplet))

    return prod_triplet