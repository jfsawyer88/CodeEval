## CodeEval
## Lowest Common Ancestor

import sys

tree = {'30':['30', 0],  '8':['30', 1], '52':['30', 1],
         '3':[ '8', 2], '20':[ '8', 2], '10':['20', 3],
        '29':['20', 3]}

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(' ')
        if tree[line[0]][1] < tree[line[1]][1]:
            a = line[1]
            b = line[0]
        else:
            a = line[0]
            b = line[1]
        while tree[a][1] > tree[b][1]:
            a = tree[a][0]

        if a != b:
            a = tree[a][0]

        sys.stdout.write(a + '\n')


f.close()
