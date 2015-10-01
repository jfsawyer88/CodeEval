## CodeEval
## Query Board

import sys

matrix = [[0 for i in xrange(256)] for i in xrange(256)]

f = open(sys.argv[1], 'r')

for line in f:

    line = line.split()
    command = line[0]
    i = int(line[1])
    if 3 == len(line):
        x = int(line[2])

    if   command == 'SetCol':
        for j in xrange(256):
            matrix[j][i] = x
    elif command == 'SetRow':
        for j in xrange(256):
            matrix[i][j] = x
    elif command == 'QueryCol':
        sys.stdout.write(str(sum([matrix[j][i] for j in xrange(256)])) + "\n")
    elif command == 'QueryRow':
        sys.stdout.write(str(sum(matrix[i])) + "\n")


f.close()
