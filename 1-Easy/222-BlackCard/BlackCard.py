## CodeEval
## Black Card

import sys

games = open(sys.argv[1], 'r')
for game in games:
    game = game.split(' | ')
    players = game[0].split(' ')
    g = int(game[1]) - 1
    while len(players) > 1:
        players.pop(g % len(players))
    sys.stdout.write(players[0] + '\n')

games.close()
