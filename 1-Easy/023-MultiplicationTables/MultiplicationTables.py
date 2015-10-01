## CodeEval
## Multiplication Tables

import sys

n = 12 #int(sys.argv[1])

mul_tab = [[(i+1)*(j+1) for j in xrange(n)] for i in xrange(n)]
width = 1 + len(str(n**2))

def f(n, num_digits):
    n = str(n)
    return ' '*(width - len(n)) + n

for line in mul_tab:
    for num in line:
        sys.stdout.write(f(num, width))
    sys.stdout.write("\n")
