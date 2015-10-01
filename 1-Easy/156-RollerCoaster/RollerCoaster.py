## CodeEval
## Roller Coaster

import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.lower()
        cap = True
        for s in line:
            if s in alpha:
                if cap:
                    sys.stdout.write(s.upper())
                else:
                    sys.stdout.write(s)
                cap = not cap
            else:
                sys.stdout.write(s)
    sys.stdout.write('\n')


f.close()
