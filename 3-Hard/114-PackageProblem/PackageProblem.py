## CodeEval
## Package Problem

import sys

def knapsack(v, w, W):
    m = [[0] * (W+1) for x in xrange(len(v)+1)]
    keep = [[0] * (W+1) for x in xrange(len(v)+1)]
    for i in xrange(1, len(v)+1):
        for j in xrange(W+1):
            if w[i-1] <= j:
                m[i][j] = max(m[i-1][j], m[i-1][j-w[i-1]] + v[i-1])
                if m[i-1][j] < m[i-1][j-w[i-1]] + v[i-1]:
                    m[i][j] = m[i-1][j-w[i-1]] + v[i-1]
                    keep[i][j] = 1
                else:
                    m[i][j] = m[i-1][j]
            else:
                m[i][j] = m[i-1][j]

    j = W
    items = []
    for i in xrange(len(v), 0, -1):
        if keep[i][j] == 1:
            items.append(str(i))
            j = j - w[i-1]

    return ','.join(reversed(items))




def knapsack(items, W):
    items = sorted(items, key=lambda item: item[1])
    m = [[0] * (W+1) for x in xrange(len(items)+1)]
    keep = [[0] * (W+1) for x in xrange(len(items)+1)]
    for i in xrange(1, len(items)+1):
        for j in xrange(W+1):
            if items[i-1][1] <= j:
                if m[i-1][j] < m[i-1][j-items[i-1][1]] + items[i-1][2]:
                    m[i][j] = m[i-1][j-items[i-1][1]] + items[i-1][2]
                    keep[i][j] = 1
                else:
                    m[i][j] = m[i-1][j]
            else:
                m[i][j] = m[i-1][j]

    j = W
    kept = []
    for i in xrange(len(items), 0, -1):
        if keep[i][j] == 1:
            kept.append(str(items[i][0]))
            j = j - items[i-1][1]

    return ','.join(reversed(kept))



f =  open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(' : ')
        W = int(line[0])


f.close()
