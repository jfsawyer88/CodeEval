## CodeEval
## Trailing String

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(',')
        if line[1] == line[0][-len(line[1]):]:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')


f.close()
