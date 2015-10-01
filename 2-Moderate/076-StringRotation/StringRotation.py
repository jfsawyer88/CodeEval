## CodeEval
## String Rotation

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(',')
        s = line[0]
        t = line[1]

        out = False
        if len(s) == len(t):
            for i in xrange(len(t)):
                if s == t[i:] + t[:i]:
                    out = True
                    break

        if out:
            sys.stdout.write('True\n')
        else:
            sys.stdout.write('False\n')


f.close()
