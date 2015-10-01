## CodeEval
## Happy Numbers

import sys

def digits(n, b=10):
    "outputs the digits of n in base b"
    res = []
    while 0 < n:
        d = n % b
        n = (n - d)/b
        res.append(d)
    #res.reverse()
    return res

bad  = [4, 16, 20, 37, 42, 58, 89, 145]
test_cases = open(sys.argv[1], 'r')

for n in test_cases:
    
    n = int(n)
    while True:
        if n in bad:
            sys.stdout.write('0\n')
            break
        if 1 == n:
            sys.stdout.write('1\n')
            break
        n = sum([i**2 for i in digits(n)])

test_cases.close()
