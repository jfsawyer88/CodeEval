## CodeEval
## Locks

import sys

def g(N, M):
    if M == 1:
        return N-1
    if M % 2 == 0:
        return 3*(N//6) + [-1,0,2,2,2,1][N%6]
    else:
        return 4*(N//6) + [-1,0,2,1,3,2][N%6]


f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        N, M = [int(n) for n in line.split(' ')]
        sys.stdout.write(str(g(N,M)) + '\n')


f.close()
