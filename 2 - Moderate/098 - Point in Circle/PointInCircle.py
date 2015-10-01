## CodeEval
## Point in Circle

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = [l.split(': ')[1] for l in line.split('; ')]
        h, k = [float(cor) for cor in line[0][1:-1].split(', ')]
        r = float(line[1])
        x, y = [float(cor) for cor in line[2][1:-1].split(', ')]
        inside = (x-h)**2 + (y-k)**2 < r**2
        sys.stdout.write(str(inside).lower() + '\n')


f.close()
