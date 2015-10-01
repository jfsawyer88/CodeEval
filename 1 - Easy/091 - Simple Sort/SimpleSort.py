## CodeEval
## Simple Sorting

import sys


f = open(sys.argv[1], 'r')

for line in f:

    line_s = line.strip().split()
    line_f = [float(s) for s in line_s]
    line_sorted = sorted(zip(line_f,line_s))

    sys.stdout.write(line_sorted[0][1])
    i = 1
    for i in xrange(1, len(line_sorted)):
        sys.stdout.write(' ' + line_sorted[i][1])

    sys.stdout.write("\n")

        
f.close()
