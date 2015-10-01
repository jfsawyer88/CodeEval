## CodeEval
## Longest Common Subsequence

import sys

LCS_memo = dict()
def LCS(s, t):
    if s == '' or t == '':
        return ''
    else:
        if (s, t) not in LCS_memo:
            if s[-1] == t[-1]:
                out = LCS(s[:-1], t[:-1]) + s[-1]
                LCS_memo[(s,t)] = out
                return out
            else:
                out1 = LCS(s[:-1], t)
                out2 = LCS(s, t[:-1])
                if len(out1) < len(out2):
                    LCS_memo[(s,t)] = out2
                    return out2
                else:
                    LCS_memo[(s,t)] = out1
                    return out1
        else:
            return LCS_memo[(s,t)]

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line != '':
        line = line.split(';')
        LCS_memo = dict() # reset to save space
                          # or don't to save time?
        sys.stdout.write(LCS(line[0], line[1]) + '\n')


f.close()
