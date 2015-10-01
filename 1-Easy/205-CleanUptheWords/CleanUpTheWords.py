## CodeEval
## Clean Up the Words

import sys
import re

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = re.sub('[^a-zA-Z]+', ' ', line).strip().lower()
        sys.stdout.write(line + '\n')


f.close()
