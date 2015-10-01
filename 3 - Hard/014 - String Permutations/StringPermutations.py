## CodeEval
## String Permutations

import sys
import itertools


f = open(sys.argv[1], 'r')

for line in f:

    line = sorted(line.strip())
    out = ''
    for string in itertools.permutations(line):
        for s in string:
            out = out + s
        out = out + ','
    sys.stdout.write(out[:-1]+ '\n')


f.close()
