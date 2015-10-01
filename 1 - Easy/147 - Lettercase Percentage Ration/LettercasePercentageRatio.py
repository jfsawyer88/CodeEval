## CodeEval
## Lettercase Percentage Ratio

import sys
import re

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    
    lower = len(''.join(re.findall('[a-z]+', line)))
    upper = len(''.join(re.findall('[A-Z]+', line)))
    
    lower = 'lowercase: ' + ('%0.2f' % (100*lower/float(len(line))))
    upper = ' uppercase: ' + ('%0.2f' % (100*upper/float(len(line))))
    sys.stdout.write(lower + upper + '\n')


f.close()
