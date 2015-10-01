## CodeEval
## Json Menu IDs

import sys
import json

f = open(sys.argv[1], 'r')

for line in f:

    line = json.loads(line)['menu']['items']
    n = 0
    for item in line:
        if None != item:
            if 'label' in item:
                n += item['id']
    sys.stdout.write(str(n) + "\n")


f.close()
