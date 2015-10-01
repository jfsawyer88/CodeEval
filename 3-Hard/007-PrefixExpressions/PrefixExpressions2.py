## CodeEval
## Prefix Expressions
## This is why I need to learn data structures!
## using a stack and working backward through
## the expression will make it much easier

import sys

if 1 != len(sys.argv):
    f = open(sys.argv[1], 'r')
else:
    import os
    f = open(os.getcwd() + '/test.txt')

ops = '+-*/'

for ex in f:

    ex = ex.strip()
    if ex:
        ex = ex.split(' ')
        stack = []
        for e in reversed(ex):
            if not e in ops:
                stack.append(int(e))
            else:
                a = stack.pop()
                b = stack.pop()
                if e == '+':
                    stack.append(a+b)
                if e == '-':
                    stack.append(a-b)
                if e == '*':
                    stack.append(a*b)
                if e == '/':
                    stack.append(a/b)

        sys.stdout.write(str(stack[0]) + '\n')


f.close()
