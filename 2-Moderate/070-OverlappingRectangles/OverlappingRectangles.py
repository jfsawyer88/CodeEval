## CodeEval
## Overlapping Rectangles

import sys

def overlaps(L1, L2):
    return not L1[1] < L2[0] or L1[0] > L2[1]

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = [int(n) for n in line.split(',')]
        X1 = sorted([line[0], line[2]])
        Y1 = sorted([line[1], line[3]])
        X2 = sorted([line[4], line[6]])
        Y2 = sorted([line[5], line[7]])

        out = overlaps(X1, X2) and overlaps(Y1, Y2)
        sys.stdout.write(str(out) + '\n')


f.close()
