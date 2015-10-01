## CodeEval
## Fibonacci Series

import sys

fib = [0, 1]

test_cases = open(sys.argv[1], 'r')

for test in test_cases:

    test = int(test)
    if test < len(fib):
        sys.stdout.write(str(fib[test]))
    else:
        i = len(fib)
        while i <= test:
            fib.append(fib[-2] + fib[-1])
            i += 1
        sys.stdout.write(str(fib[test]))
    sys.stdout.write("\n")


test_cases.close()
