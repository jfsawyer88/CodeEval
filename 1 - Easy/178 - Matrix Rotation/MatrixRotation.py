## CodeEval
## Matrix Rotation

import sys

f = open(sys.argv[1], 'r')

for M in f:

    M = M.strip()
    if M:
        M = M.split(' ')
        N = int(len(M)**0.5)
        out = []
        for i in xrange(N):
            for j in xrange((N-1)*N, -1, -N):
                out.append(M[i+j])
        sys.stdout.write(' '.join(out) + '\n')


f.close()
