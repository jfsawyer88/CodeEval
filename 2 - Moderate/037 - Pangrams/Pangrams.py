## CodeEval
## Pangrams

import sys
import re

#alpha = 'abcdefghijklmnopqrstuvwxyz'

f = open(sys.argv[1], 'r')

for line in f:

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    line = line.strip()
    if line:
        line = line.lower()
        line = re.sub('[^a-z]', '', line)
        #line = re.sub('['+line+']', '', alpha)
        out = ''
        for s in alpha:
            if s not in line:
                out = out + s

        if out:
            sys.stdout.write(out + '\n')
        else:
            sys.stdout.write('NULL\n')


f.close()
