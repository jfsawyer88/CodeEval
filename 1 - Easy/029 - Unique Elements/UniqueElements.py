## CodeEval
## Unique Elements

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = [int(i) for i in test.split(',')]
    
    sys.stdout.write(str(test[0]))
    
    i = 1
    while i < len(test):
        if test[i-1] != test[i]:
            sys.stdout.write(',' + str(test[i]))
        i += 1
    sys.stdout.write("\n")

test_cases.close()
