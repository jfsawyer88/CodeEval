## CodeEval
## Multiples of a Number

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:

    test = test.split(',')
    m = int(test[0])
    n = int(test[1])

    i = 1
    while i*n < m:
        i = i * 2

    low  = i // 2
    high = i
    while 1 != abs(high - low):
        mid = (low+high)//2
        if mid*n >= m:
            high = mid
        elif mid*n < m:
            low = mid
            
    sys.stdout.write(str(high * n))
    sys.stdout.write("\n")


test_cases.close()
