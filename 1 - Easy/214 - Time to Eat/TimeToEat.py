## CodeEval
## Time to Eat

import sys

f = open(sys.argv[1], 'r')

for times in f:

    times = times.strip().split(' ')
    to_sort = [map(int, time.split(':')) for time in times]
    sort_order = [3600*time[0] + 60*time[1] + time[0] for time in to_sort]
    out = [time[1] for time in sorted(zip(sort_order, times), reverse=True)]
    sys.stdout.write(' '.join(out) + '\n')


f.close()
