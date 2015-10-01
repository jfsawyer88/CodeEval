## CodeEval
## Sum of Integers

import sys

def LSA(A):
    """Largest Sum Array"""
    max_now = A[0]
    max_all = A[0]
    for n in A[1:]:
        max_now = max(n, max_now + n)
        max_all = max(max_all, max_now)
    return max_all


f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = [int(n) for n in line.split(',')]
        sys.stdout.write(str(LSA(line)) + '\n')


f.close()
