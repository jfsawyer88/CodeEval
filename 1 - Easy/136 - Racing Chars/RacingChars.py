## CodeEval
## Racing Chars

import sys

f = open(sys.argv[1], 'r')

path = f.readline().strip()

if 'C' in path:
    path = path.split('C')
else:
    path = path.split('_')

sys.stdout.write(path[0] + '|' + path[1] + '\n')    
pos = len(path[0])

for path in f:

    path = path.strip()
    if 'C' in path:
        path = path.split('C')
    else:
        path = path.split('_')

    pos_next = len(path[0])
    sys.stdout.write(path[0] + '/|\\'[1 + pos_next - pos] + path[1] + '\n')
    pos = pos_next


f.close()
