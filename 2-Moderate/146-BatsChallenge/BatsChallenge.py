## CodeEval
## Bats Challenge

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = [int(n) for n in line.strip().split()]
    l = line[0]
    d = line[1]
    bats = line[3:]

    n_bats = 0
    if bats:
        spots = bats[0] - d - 6 + 1
        n_bats += (spots + (-spots%d))//d

        i = 1
        while i < len(bats):
            spots = bats[i] - bats[i-1] - 2*d + 1
            n_bats += (spots + (-spots%d))//d
            i += 1

        spots = l - bats[-1] - d - 6 + 1
        n_bats += (spots + (-spots%d))//d
    else:
        spots = l - 12 + 1
        n_bats +=(spots + (-spots%d))//d

    sys.stdout.write(str(n_bats) + '\n')


f.close()
