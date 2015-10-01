## CodeEval
## Find the Highest Score

import sys

f = open(sys.argv[1], 'r')

for contest in f:

    contest = contest.strip()
    if contest:
        contest = [[int(score) for score in artist.split(' ')] for artist in contest.split(' | ')]
        out = [str(max([artist[i] for artist in contest])) for i in xrange(len(contest[0]))]
        sys.stdout.write(' '.join(out) + '\n')


f.close()
