## CodeEval
## Fizz Buzz

import sys

print
for line in sys.stdin:
    print line
print
print
print

if 1 != len(sys.argv):
    test_cases = open(sys.argv[1], 'r')
else:
    import os, inspect
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    test_cases = open(path + '/test.txt')

for test in test_cases:

    # split the line into the inputs
    # and convert string to integers
    line = test.split()
    x = int(line[0])
    y = int(line[1])
    n = int(line[2])

    i = 1 # initialize at one
    while True:

        # flag so that we print the number
        # only if F or B has not been printed
        printed = False
        
        if 0 == i % x:                # print F if divisible by x
            sys.stdout.write('F')
            printed = True
        if 0 == i % y:                # print B if divisible by y
            sys.stdout.write('B')
            printed = True
        if printed == False:          # print i if nothing else has
            sys.stdout.write(str(i))  # been printed
            
        if i < n:                     # add a space and continue
            sys.stdout.write(' ')     # until i == n
        else:
            break

        i += 1 # don't forget to increment i!

    sys.stdout.write('\n')

test_cases.close()
