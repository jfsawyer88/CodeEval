## CodeEval
## First Non-Repeated Character

import sys

f = open(sys.argv[1], 'r')

for s in f:

    s = s.strip()
    good = dict()
    bad  = set()

    for i in xrange(len(s)):
        if s[i] in good:
            del good[s[i]]
            bad.add(s[i])
        elif s[i] not in bad:
            good[s[i]] = i

    if good:
        sys.stdout.write(sorted([[good[t], t] for t in good])[0][1] + '\n')


f.close()
