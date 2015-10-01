## CodeEval
## Lowest Unique Number

import sys

f = open(sys.argv[1], 'r')

for game in f:

    game = [int(n) for n in game.split()]
    good = set()
    bad  = set()

    for n in game:
        if n in good:
            good.remove(n)
            bad.add(n)
        elif n not in bad:
            good.add(n)

    if 0 == len(good):
        sys.stdout.write('0\n')
    else:
        sys.stdout.write(str(1 + game.index(min(good))) + "\n")

f.close()
