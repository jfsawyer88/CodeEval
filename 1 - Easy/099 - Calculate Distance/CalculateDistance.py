## CodeEval
## Find a Writer

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()[1:-1].split(') (')
    p1 = [int(n) for n in line[0].split(', ')]
    p2 = [int(n) for n in line[1].split(', ')]

    dist = int(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5)
    sys.stdout.write(str(dist) + "\n")


f.close()
