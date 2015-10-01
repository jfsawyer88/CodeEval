## CodeEval
## Slang Flavor

import sys
#import re

slang = [', yeah!', ', this is crazy, I tell ya.', ', can U believe this?',
         ', eh?', ', aw yea.', ', yo.', '? No way!', '. Awesome!']
i = 0
change = False

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        #line = re.findall('[^\!\.\?]+[\!\.\?]', s)
        for l in line:
            if l == '.' or l == '!' or l == '?':
                if change:
                    sys.stdout.write(slang[i])
                    i = (i+1) % len(slang)
                else:
                    sys.stdout.write(l)
                change = not change
            else:
                sys.stdout.write(l)
        sys.stdout.write('\n')
        


f.close()
