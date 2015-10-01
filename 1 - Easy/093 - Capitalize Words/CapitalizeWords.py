## CodeEval
## Capitalize Words

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split()

    sys.stdout.write(line[0][0].upper() + line[0][1:])
    for i in xrange(1, len(line)):
        sys.stdout.write(' ' + line[i][0].upper() + line[i][1:])
    sys.stdout.write("\n")

f.close()
