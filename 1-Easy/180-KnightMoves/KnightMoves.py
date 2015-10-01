## CodeEval
## Knight Moves

import sys

al = 'abcdefgh'
al_dict = {al[i]: i for i in xrange(8)}

f = open(sys.argv[1], 'r')

for pos in f:

    pos = pos.strip()
    x = al_dict[pos[0]]
    y = int(pos[1])-1
    new_coors = [[x-2, y-1], [x-2, y+1],
                 [x-1, y-2], [x-1, y+2],
                 [x+1, y-2], [x+1, y+2],
                 [x+2, y-1], [x+2, y+1]]
    out = []
    for coor in new_coors:
        if 0 <= coor[0] < 8 and 0 <= coor[1] < 8:
            out.append(al[coor[0]] + str(coor[1]+1))

    sys.stdout.write(' '.join(out) + '\n')


f.close()
