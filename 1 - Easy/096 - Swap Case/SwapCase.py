## CodeEval
## Swap Case

import sys

f = open(sys.argv[1], 'r')

for line in f:
    sys.stdout.write(line.swapcase())
    
sys.stdout.write("\n")
f.close()
