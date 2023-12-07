import re
import numpy as np
BAG_CONTENTS = {'red': 12, 'green': 13, 'blue': 14}

with open("2023\inputs\input2.txt", 'r') as f:
    lines = f.readlines()

total_games = 0
total_power = 0
for i in lines:
    min_tiles = {'red': 0, 'green': 0, 'blue': 0}
    possible = True
    gameId, turns = i.split(":")
    for t in turns.split(";"):
        tiles = t.split(',')
        for tile in tiles:
            curr = tile.split()
            if min_tiles[curr[1]] < int(curr[0]):
                min_tiles[curr[1]] = int(curr[0])
            if BAG_CONTENTS[curr[1]] < int(curr[0]):
                possible = False
    total_power += np.prod(list(min_tiles.values()))
    if possible:
        total_games += int(re.findall(r'\d+', gameId)[0])

print(f"sum of valid game ids: {total_games}")
print(f"sum of game powers: {total_power}")
