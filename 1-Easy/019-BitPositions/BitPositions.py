## CodeEval
## Bit Positions

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


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    
    test = test.split(',')
    n  = int(test[0])
    p1 = int(test[1]) - 1
    p2 = int(test[2]) - 1

    n_bin = digits(n, 2)

    if n_bin[p1] == n_bin[p2]:
        sys.stdout.write('true')
    else:
        sys.stdout.write('false')
    sys.stdout.write("\n")


test_cases.close()
