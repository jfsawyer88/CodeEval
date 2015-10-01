## CodeEval
## Beautiful Strings

import sys

f = open(sys.argv[1], 'r')

for s in f:

    s = s.lower()
    alpha = {a:0 for a in 'abcdefghijklmnopqrstuvwxyz'}
    for l in s:
        if l in alpha:
            alpha[l] += 1
    alpha = sorted(alpha.values())
    print sum([(i + 1)*alpha[i] for i in xrange(26)] )

f.close()
