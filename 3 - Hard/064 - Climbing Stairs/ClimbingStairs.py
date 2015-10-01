## CodeEval
## Climbing Stairs
## NB: equivalent to n'th fibonacci number

import sys


def mp(M, N):
    return [[M[0][0]*N[0][0] + M[0][1]*N[1][0], M[0][0]*N[0][1] + M[0][1]*N[1][1]],
            [M[1][0]*N[0][0] + M[1][1]*N[1][0], M[1][0]*N[0][1] + M[1][1]*N[1][1]]]

def square(M, n=1):
    for i in xrange(n):
        M = mp(M, M)
    return M

def exponent(M, n):
    binary = []
    i = 0
    while 0 < n:
        d = n % 2
        n = (n - d)/2
        if d:
            binary.append(i)
        i += 1
    sub = [square(M, i) for i in binary]
    out = [[1,0],
           [0,1]]
    for N in sub:
        out = mp(N, out)
    return out


def fib(n):
    return exponent([[0,1],[1,1]], n)[0][1]


f = open(sys.argv[1], 'r')

for n in f:

    n = n.strip()
    if n:
        sys.stdout.write(str(fib(int(n)+1)) + '\n')


f.close()
