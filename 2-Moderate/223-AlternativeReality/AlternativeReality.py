## CodeEval
## Alternative Reality

import sys

coins = [1, 5, 10, 25, 50]
ways = [1] + [0] * 100
for coin in coins:
    for j in xrange(coin, len(ways)):
        ways[j] += ways[j - coin]

goals = open(sys.argv[1], 'r')

for goal in goals:
    sys.stdout.write(str(ways[int(goal)]) + '\n')

goals.close()
