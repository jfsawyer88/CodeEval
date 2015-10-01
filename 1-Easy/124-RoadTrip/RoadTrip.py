## CodeEval
## Road Trip

import sys

f = open(sys.argv[1], 'r')

for line in f:

    dists = sorted([int(city.split(',')[1]) for city in line.strip()[:-1].split(';')])
    sys.stdout.write(str(dists[0]))
    for i in xrange(1, len(dists)):
        sys.stdout.write(',' + str(dists[i] - dists[i-1]))
    sys.stdout.write('\n')


f.close()
