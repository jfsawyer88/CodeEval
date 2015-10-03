## CodeEval
## Chain Inspection

import sys

if 1 != len(sys.argv):
    f = open(sys.argv[1], 'r')
else:
    import os
    f = open(os.getcwd() + '/test.txt')


for chain in f:

    chain = [link.split('-') for link in chain.strip().split(';')]
    next_node = 'BEGIN'
    while chain:
        i = 0
        found = False
        while i < len(chain):
            if chain[i][0] == next_node:
                next_node = chain.pop(i)[1]
                found = True
            i += 1
        if not found:
            break
    if next_node == 'END' and not chain: # if it reached the end
        sys.stdout.write('GOOD' + '\n')  # and all nodes were hit
    else:
        sys.stdout.write('BAD'  + '\n')


f.close()
