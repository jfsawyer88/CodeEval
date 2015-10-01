## CodeEval
## Armstrong Numbers

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

f = open(sys.argv[1], 'r')

for n in f:
    n = int(n)
    num_digits = len(str(n))
    sys.stdout.write(str(n == sum([d**num_digits for d in digits(n)])) + "\n")

f.close()
