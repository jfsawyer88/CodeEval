## CodeEval
## Data Recovery

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        sentence, hint = line.split(';')
        sentence = sentence.split(' ')
        hint = [int(h)-1 for h in hint.split(' ')]
        hint.append((len(sentence)*(len(sentence)-1)/2) - sum(hint))
        out = [word[1] for word in sorted(zip(hint, sentence))]
        sys.stdout.write(' '.join(out) + '\n')


f.close()
