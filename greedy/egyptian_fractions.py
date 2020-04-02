# Every positive fraction can be represented as sum of 
# unique unit fractions. A fraction is unit fraction if 
# numerator is 1 and denominator is a positive integer, 
# or example 1/3 is a unit fraction. Such a 
# representation is called Egyptian Fraction as it 
# was used by ancient Egyptians. 

import math
import sys

def egyptian_fractions(num, den):
    denom_list = list()
    while num > 0:
        new_den = math.ceil(den / num)
        denom_list.append(new_den)

        num = (num * new_den) - den
        den = den * new_den

    return denom_list

if __name__ == '__main__':
    arr = input()
    arr = arr.split(' ')
    arr = [int(i) for i in arr]
    if len(arr) > 2:
        print('only 2 integers expected')
        sys.exit(0)

    # printing only denominators since all numerators are 1
    # for egyptian fractions
    print(egyptian_fractions(arr[0], arr[1]))