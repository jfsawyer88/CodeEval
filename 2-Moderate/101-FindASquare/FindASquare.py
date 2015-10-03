## CodeEval
## Find A Square
## by using dot products

import sys

if 1 != len(sys.argv):
    f = open(sys.argv[1], 'r')
else:
    import os
    f = open(os.getcwd() + '/test.txt', 'r')

# vector functions
def add(v,w):
    '''vector addition'''
    return [v[0] + w[0], v[1] + w[1]]
def diff(v, w):
    '''vector subtraction'''
    return [v[0] - w[0], v[1] - w[1]]
def dot(v, w):
    '''eucliden dot product of given vectors'''
    return v[0]*w[0] + v[1]*w[1]

# main loop
for points in f:

    a,b,c,d = [map(int, point[1:-1].split(',')) for point in points.strip().split(', ')]

    is_square = False
    ps = [[b,c], [c,d], [d,b]]
    pd = [d, b, c]
    i = 0
    while i < 3:
        if 0 == dot(diff(a, ps[i][0]),
                    diff(a, ps[i][1])):
            found = True
            break
        i += 1

    if i<3:
        b, c = ps[i]
        d = pd[i]
        print d == add(a, add(diff(b,a), diff(c,a)))




f.close()
