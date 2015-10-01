## CodeEval
## Minimum Path Sum

import sys


def MPS(M, i = None, j = None, memo = None):

    if memo == None:
        memo = dict()
    if i == None:
        i = len(M) - 1
        j = len(M) - 1

    if i == 0:
        return sum([M[0][k] for k in xrange(j+1)])
    if j == 0:
        return sum([M[k][0] for k in xrange(i+1)])

    if (i,j) in memo:
        return memo[(i, j)]
    else:
        out1 = M[i][j] + MPS(M, i-1,   j, memo)
        out2 = M[i][j] + MPS(M,   i, j-1, memo)
        if out1 < out2:
            memo[(i,j)] = out1
            return out1
        else:
            memo[(i,j)] = out2
            return out2


f = open(sys.argv[1], 'r')

n = f.readline()
while n:
    M = [[int(m) for m in f.readline().split(',')] for i in xrange(int(n))]
    sys.stdout.write(str(MPS(M)) + '\n')
    n = f.readline()

f.close()
