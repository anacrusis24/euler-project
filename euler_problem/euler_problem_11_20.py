'''
---------- euler_problem_11_20.py ----------
Time    :  2022/05/23 19:44:15
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  Function to solve Euler problems 11 - 20
'''


##### Imports #####
import numpy as np
from euler_problem_1_10 import find_factor_pairs

##### Define Functions #####
def greatest_product(num_adjacent):
    '''
    @greatest_product
    Function finds the greatest product of adjacent numbers in the block of numbers
    
    @Input
    num_adjacent: number of adjacent numbers to compute in the product
    
    @Output
    max_product: the greatest product in the block of numbers
    '''
    # The block of numbers to find the greatest product
    str_num = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''

    # Make the string into multi-dimensional array
    block = np.array(str_num.split(), dtype='int')
    block = block.reshape(20, 20)
    flip_block = np.fliplr(block)

    # Create empty list of products
    products = []

    # Loops to calculate the products 
    for i in range(20 - num_adjacent + 1):
        for j in range(20 - num_adjacent + 1):
            # Calculate the products
            horizontal_prod = np.prod(block[i][j:(j+num_adjacent)])
            vertical_prod = np.prod(block[i:(i+num_adjacent), j:(j+1)])
            diagonal_prod_1 = np.prod(np.diag(block[i:], k=j)[:num_adjacent])
            diagonal_prod_2 = np.prod(np.diag(flip_block[i:], k=j)[:num_adjacent])

            # Append them to list 
            products.append(horizontal_prod)
            products.append(vertical_prod)
            products.append(diagonal_prod_1)
            products.append(diagonal_prod_2)
    
    max_product = max(products)

    return max_product


def tri_num_divisor(num_divisors):
    '''
    @tri_num_divisor
    Function find the first triangle number with number of divisors greater than num_divisors 
    
    @Input
    num_divisors: the number of divisors the triangle number should exceed
    
    @Output
    tri_num: the first triangle number with the desired amount of divisors
    '''
    # Initialize variables
    tri_number_found = False
    curr_num = 1
    curr_tri_num = 1

    # Loop generates triangle numbers and checks factors for each new number
    while not tri_number_found:
        # Check the number of divisors of the current triangle number
        divisors = np.count_nonzero(np.array(find_factor_pairs(curr_tri_num)))
        if divisors > num_divisors:
            break
        
        # Increment the numbers
        curr_num += 1
        curr_tri_num += curr_num

    return curr_tri_num


def first_n_digits_sum(n):
    '''
    @first_n_digits_sum
    Function finds the first n digits of the sum of the block of numbers
    
    @Input
    n: the number of digits to find
    
    @Output
    digits: a string of n digits of the sum of the block of numbers
    '''
    str_num = '''
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690
'''
    
    # Create array of numbers
    block = np.array(str_num.splitlines())[1:]

    # Calculate sum
    running_sum = ''
    num_number = len(block)
    num_digits = len(block[0])
    remainder = 0

    for j in range(num_digits):
        col_sum = remainder 
        for i in range(num_number):
            col_sum += int(block[i][num_digits - 1 - j])
        
        col_sum = str(col_sum)
        if j == (num_digits - 1):
            running_sum = col_sum + running_sum          
        else:
            digit = col_sum[-1]
            running_sum = digit + running_sum
            remainder = int(col_sum[:(len(col_sum)-1)])

    return running_sum[:n]


def collatz_sequence(start_num):
    '''
    @collatz_sequence
    Function generates the Collatz sequence for the given starting number
    
    @Input
    start_num: the starting number for the collatz_sequence
    
    @Output
    sequence: the collatz sequence
    '''
    sequence = [start_num]

    curr_num = start_num
    while curr_num != 1:
        if curr_num % 2 == 0:
            curr_num /= 2
        else:
            curr_num = 3 * curr_num + 1
        
        sequence.append(int(curr_num))
    
    return sequence


def longest_collatz_chain(max_start_num):
    '''
    @longest_collatz_chain
    Function finds the starting number that produces the longest Collatz chain
    
    @Input
    max_start_num: the max possible starting number
    
    @Output
    long_chain_num: the number that produces the longest chain
    '''
    longest_chain = 0
    long_chain_num = 0

    for i in range(1, max_start_num):
        curr_num = i
        count = 1

        # The collatz part
        while (curr_num != 1):
            if curr_num % 2 == 0:
                curr_num /= 2
                count += 1
            else:
                curr_num = 3 * curr_num + 1

        # Find number that produces longest chain
        if count > longest_chain:
            longest_chain = count
            long_chain_num = i

    return long_chain_num


def lattice_paths(height, width):
    '''
    @lattice_paths
    Function finds how many routes there are to get from the top left corner of the lattice to the bottom right corner using only down and right movements
    
    @Input
    height: the height of the lattice
    width: the width of the lattice
    
    @Output
    num_paths: the number of paths to the bottom right corner
    '''
    # Make lattice with boundary conditions
    lattice = np.zeros((height + 1, width + 1), dtype='int64')
    lattice[:,height:height+1] = 1
    lattice[width:] = 1
    lattice[height, width] = 0

    # Fill in lattice al la pascals triangle
    for i in range(height - 1, -1, -1):
        for j in range(width - 1, -1, -1):
            lattice[i, j] = lattice[i, j + 1] + lattice[i + 1, j]

    return lattice[0, 0]


def power_digit_sum(power):
    '''
    @power_digit_sum
    Function calculates the sum of the digits of the number 2^power
    
    @Input
    power: the power to raise 2 to
    
    @Output
    pwd_sum: the sum of the digits of the power of 2
    '''
    pwd_sum = 0
    str_num = str(2**power)

    # Peel off each digit and add to sum
    for digit in str_num:
        pwd_sum += int(digit)

    return pwd_sum


def number_letter_count(max_num):
    '''
    @number_letter_count
    Function counts the sum of letters for each spelled number up to the max_num (inclusive)
    
    @Input
    max_num: the max number to include in the sum
    
    @Output
    letter_count: the letter count of the sum 
    '''
    # Dict to hold small counts
    ones_dict = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    teens_dict = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    tens_dict = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    hundreds_dict = {100:'hundred'}
    thousands_dict = {1000:'thousand'}

    # Initialize running count
    letter_count = 0

    for i in range(1, max_num + 1):
        # Get current letter count
        if i < 10:
            curr_count = len(ones_dict[i])
        elif i < 20:
            curr_count = len(teens_dict[i])
        elif i < 100:
            first_digit = str(i)[0]
            second_digit = str(i)[1]
            curr_count = len(tens_dict[int(first_digit + '0')]) + len(ones_dict[int(second_digit)])
        elif i < 1000:
            first_digit = str(i)[0]
            second_digit = str(i)[1]
            third_digit = str(i)[2]
            if (second_digit == '0') and (third_digit == '0'):
                curr_count = len(ones_dict[int(first_digit)]) + len(hundreds_dict[100])
            elif (second_digit == '0') and (third_digit != '0'):
                curr_count =  len(ones_dict[int(first_digit)]) + len(hundreds_dict[100]) + len('and') + len(ones_dict[int(third_digit)])
            elif (second_digit == '1'):
                curr_count =  len(ones_dict[int(first_digit)]) + len(hundreds_dict[100]) + len('and') + len(teens_dict[int(str(i)[1:])])
            else:
                curr_count =  len(ones_dict[int(first_digit)]) + len(hundreds_dict[100]) + len('and') + len(tens_dict[int(second_digit + '0')]) + len(ones_dict[int(third_digit)])
        else:
            first_digit = str(i)[0]
            second_digit = str(i)[1]
            curr_count = len(ones_dict[int(first_digit)]) + len(thousands_dict[1000])

        # Add to running sum
        letter_count += curr_count

    return letter_count


def max_path_sum():
    '''
    @max_path_sum
    Function finds the maximum sum of the path from top to bottom in the triangle
    
    @Output
    max_sum:
    '''
    str_triangle = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

    # Create array of numbers
    str_triangle = np.array(str_triangle.splitlines())[1:]
    triangle = []

    # Convert to int and separate values
    for line in str_triangle:
        line = np.array(line.split()).astype('int64')
        triangle.append(line)
    
    triangle = np.array(triangle)
    curr_row = []

    for i in range(len(triangle) - 1, 0, -1):
        # Get the two rows to do the addition
        top_row = triangle[i - 1]
        bot_row = triangle[i]

        for j in range(len(top_row)):
            num_sum = top_row[j] + max(bot_row[j], bot_row[j + 1])
            curr_row.append(num_sum)

        triangle[i - 1] = np.array(curr_row)
        curr_row = []
    return triangle[0][0]