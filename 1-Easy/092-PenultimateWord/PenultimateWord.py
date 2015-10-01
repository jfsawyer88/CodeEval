## CodeEval
## Penultimate Word

import sys

f = open(sys.argv[1], 'r')

for line in f:
    sys.stdout.write(line.split()[-2] + "\n")

f.close()
