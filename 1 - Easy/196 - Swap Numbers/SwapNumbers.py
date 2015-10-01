## CodeEval
## Swap Numbers

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = [s[-1] + s[1:-1] + s[0] for s in line.split(' ')]
        sys.stdout.write(' '.join(line) + '\n')


f.close()
