## CodeEval
## Minimum Coins

import sys

coins = [5, 3, 1]

change_memo = dict()
def change(n):
    if n in change_memo:
        return change_memo[n]
    if  n == 0:
        return 0
    if n < 0:
        return float('inf')
    res = 1 + min(change(n-5), change(n-3), change(n-1))
    change_memo[n] = res
    return res

f = open(sys.argv[1], 'r')

for n in f:

    n = n.strip()
    if n:
        sys.stdout.write(str(change(int(n))) + '\n')


f.close()
