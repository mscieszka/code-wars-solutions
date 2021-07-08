"""
Given an array of positive or negative integers I= [i1,..,in] produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. 
The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]

[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:
    It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

    In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
"""


import sympy


def sum_for_list(lst):
    prime_factors = {} # key=prime_factor, val=values which contain given prime factor

    # determining prime factors for each value in the lst
    for val in lst:
        for i in range(val//2):
            if sympy.isprime(i) and val % i == 0:
                prime_factors.setdefault(i,[]).append(val)

    # array of arrays where values are: prime factor and sum of the numbers for which given value is a prime factor
    result = [[key, sum(prime_factors[key])] for key in sorted(prime_factors)]
    
    return result


print(sum_for_list([15, 21, 24, 30, 45]))
