## CodeEval
## Sum of Digits

import sys

def sum_of_digits(n, b=10):
    res = 0
    while 0 < n:
        d = n % b
        n = (n - d)/b
        res += d
    return res

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    sys.stdout.write(str(sum_of_digits(int(test))))
    sys.stdout.write("\n")

test_cases.close()
