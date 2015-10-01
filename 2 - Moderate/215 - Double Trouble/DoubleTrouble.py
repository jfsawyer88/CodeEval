## CodeEval
## Double Trouble

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        size = len(line)/2
        part1 = line[size:]
        part2 = line[:size]
        out = 1
        for i in xrange(size):
            stars = ('*' == part1[i]) + ('*' == part2[i])
            if stars:
                out *= stars
            else:
                if part1[i] != part2[i]:
                    out = 0
                    break

        sys.stdout.write(str(out) + '\n')


f.close()
