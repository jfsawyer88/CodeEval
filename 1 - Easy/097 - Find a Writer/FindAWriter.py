## CodeEval
## Find a Writer

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split('|')
    string = line[0]
    key = [int(i) for i in line[1].split()]

    for k in key:
        sys.stdout.write(string[k-1])
    sys.stdout.write("\n")


f.close()
