## CodeEval
## Read More

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if len(line) > 55:
        after = line[40]
        line = line[:40]
        if ' ' in line and after != ' ':
            line = ' '.join(line.split(' ')[:-1])
        line = line +  '... <Read More>\n'
    else:
        line = line + '\n'
    sys.stdout.write(line)


f.close()
