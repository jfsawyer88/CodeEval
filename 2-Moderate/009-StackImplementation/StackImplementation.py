## CodeEval
## Stack Implementation

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split(' ')
    sys.stdout.write(line[-1])
    i = 2
    while i < len(line):
        sys.stdout.write(' ' + line[-(i+1)])
        i += 2
    sys.stdout.write('\n')


f.close()
