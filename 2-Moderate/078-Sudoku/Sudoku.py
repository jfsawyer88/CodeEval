## CodeEval
## Sudoku

import sys


def sudokuq(mat):

    size = len(mat)
    sqrt = int(size**0.5)
    for i in xrange(size):
        good = set(range(1, size+1))
        for n in mat[i]:
            if n in good:
                good.remove(n)
            else:
                return False

    for j in xrange(size):
        good = set(range(1, size+1))
        for n in [mat[k][j] for k in xrange(size)]:
            if n in good:
                good.remove(n)
            else:
                return False

    for i in range(0, size, sqrt):
        for j in range(0, size, sqrt):
            good = set(range(1, size+1))
            sub = [M[0+j:sqrt+j] for M in mat[0+i:sqrt+i]]
            for l in sub:
                for n in l:
                    if n in good:
                        good.remove(n)
                    else:
                        return False

    return True


f = open(sys.argv[1], 'r')

for mat in f:

    mat = mat.strip()
    if mat:
        mat = mat.split(';')
        size = int(mat[0])
        mat = [int(n) for n in mat[1].split(',')]
        mat = [mat[i:i+size] for i in xrange(0, len(mat), size)]
        sys.stdout.write(str(sudokuq(mat)) + '\n')


f.close()
