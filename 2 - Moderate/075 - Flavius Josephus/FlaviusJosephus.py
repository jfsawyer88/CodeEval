## CodeEval
## Flavius Josephus

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(',')
        n = int(line[0])
        m = int(line[1])

        i = 0
        circle = [str(j) for j in xrange(n)]
        out = []
        while circle:
            i = (i + (m-1)) % len(circle)
            out.append(circle.pop(i))

        sys.stdout.write(' '.join(out) + '\n')


f.close()
