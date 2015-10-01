## CodeEval
## Remove Characters

import sys
import re

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(', ')
        sys.stdout.write(re.sub('['+line[1]+']', '', line[0]) + '\n')


f.close()
