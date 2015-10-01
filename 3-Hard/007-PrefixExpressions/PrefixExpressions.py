## CodeEval
## Prefix Expressions

import sys

ops = '+*/'

def parse_prefix_ex(ex):
    if 3 == len(ex):
        return ex
    elif 1 == len(ex):
        return ex[0]
    else:
        if ex[1] in ops:
            op_cnt = 1
            n_cnt = 0
            i = 2
            while n_cnt <= op_cnt :
                if ex[i] in ops:
                    op_cnt += 1
                else:
                    n_cnt += 1
                i += 1
            return [ex[0],
                    parse_prefix_ex(ex[1:i]),
                    parse_prefix_ex(ex[i:])]
        else:
            return [ex[0],
                    ex[1],
                    parse_prefix_ex(ex[2:])]

def eval_prefix_ex(ex):
    if isinstance(ex, str):
        return int(ex)
    else:
        if '+' == ex[0]:
            return eval_prefix_ex(ex[1]) + eval_prefix_ex(ex[2])
        if '*' == ex[0]:
            return eval_prefix_ex(ex[1]) * eval_prefix_ex(ex[2])
        if '/' == ex[0]:
            return eval_prefix_ex(ex[1]) / eval_prefix_ex(ex[2])



f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(' ')
        sys.stdout.write(str(eval_prefix_ex(parse_prefix_ex(line))) + '\n')



f.close()
