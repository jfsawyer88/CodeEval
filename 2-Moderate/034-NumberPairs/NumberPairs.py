## CodeEval
## Number Pairs

import sys

f = open(sys.argv[1], 'r')

for line in f:

    arr, X = line.split(';')
    arr = [int(n) for n in arr.split(',')]
    #arr = sorted(set([int(n) for n in arr.split(',')]))
    X = int(X)

    out = []
    i = 0
    j_max = len(arr)-1
    while i <= j_max:
        j = j_max
        while i <= j:
            a = arr[i] + arr[j]
            if a == X:
                j_max = j-1
                out.append(str(arr[i]) + ',' + str(arr[j]))
                break
            if a < X:
                break
            j -= 1
        i += 1

    if out:
        sys.stdout.write(';'.join(out) + '\n')
    else:
        sys.stdout.write('NULL\n')


f.close()
