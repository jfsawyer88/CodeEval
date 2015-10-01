## CodeEval
## Nice Angles

import sys

f = open(sys.argv[1], 'r')

for angle in f:

    angle = float(angle)
    deg = int(angle)
    frac = int((angle - deg) * 3600)
    second = frac % 60
    minute = (frac - second)/60
    
    if second < 10:
        second = '0' + str(second) + '\"'
    else:
        second = str(second) + '\"'

    if minute < 10:
        minute = '0' + str(minute) + '\''
    else:
        minute = str(minute) + '\''

    deg = str(deg) + '.'

    sys.stdout.write(deg + minute + second + '\n')


f.close()
