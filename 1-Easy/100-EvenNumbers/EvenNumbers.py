## CodeEval
## Even Numbers

import sys

f = open(sys.argv[1], 'r')

for n in f:
    sys.stdout.write(str((int(n) + 1) % 2) + "\n")

f.close()
