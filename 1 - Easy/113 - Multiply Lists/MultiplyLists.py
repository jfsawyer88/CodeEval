## CodeEval
## Swap Elements

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split(' | ')
    v1 = [int(n) for n in line[0].split()]
    v2 = [int(n) for n in line[1].split()]

    sys.stdout.write(str(v1[0]*v2[0]))
    for i in xrange(1, len(v1)):
        sys.stdout.write(' ' + str(v1[i]*v2[i]))
    sys.stdout.write("\n")


f.close()
