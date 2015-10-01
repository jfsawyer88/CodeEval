## CodeEval
## Happy Numbers

import sys


f = open(sys.argv[1], 'r')

for line in f:
    
    line = line.split(',')
    n = int(line[0])
    m = int(line[1])
    
    sys.stdout.write(str(n - m*(n//m)) + "\n")

f.close()
