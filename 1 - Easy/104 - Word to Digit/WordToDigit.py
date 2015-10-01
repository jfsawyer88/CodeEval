## CodeEval
## Word to Digit

import sys

digits = {'zero':'0', 'one':'1',   'two':'2', 'three':'3', 'four':'4',
          'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip().split(';')
    for digit in line:
        sys.stdout.write(digits[digit])
    sys.stdout.write("\n")


f.close()
