## CodeEval
## Filename Pattern

import sys
import re

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split(' ')
    pat = '^' + line[0] + '$'
    pat = pat.replace('.', '\.').replace('*', '.*').replace('?', '.')
    pat = re.compile(pat)
    files = line[1:]
    out = [fil for fil in files if pat.match(fil)]
    if out:
        sys.stdout.write(' '.join(out) + '\n')
    else:
        sys.stdout.write('-\n')


f.close()
