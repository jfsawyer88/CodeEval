## CodeEval
## Detecting Cycles

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = [int(n) for n in line.strip().split(' ')]
    i = 1
    while i < len(line):
        if line[i] in line[:i]:
            cycle = line[line[:i].index(line[i]):i]
            break
        i += 1

    if i == len(line):
        cycle = [line[-1]]

    sys.stdout.write(str(cycle[0]))
    for n in cycle[1:]:
        sys.stdout.write(' ' + str(n))
    sys.stdout.write('\n')


f.close()
