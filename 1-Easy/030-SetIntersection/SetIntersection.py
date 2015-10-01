## CodeEval
## Unique Elements

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    
    test = test.split(';')
    a = {int(i) for i in test[0].split(',')}
    b = {int(i) for i in test[1].split(',')}
    a_and_b = sorted(a & b)

    if [] == a_and_b:
        sys.stdout.write("\n")
    else:
        sys.stdout.write(str(a_and_b[0]))
        i = 1
        while i < len(a_and_b):
            sys.stdout.write(',' + str(a_and_b[i]))
            i += 1
        sys.stdout.write("\n")
    
test_cases.close()
