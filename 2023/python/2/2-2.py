import re
from functools import reduce
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

bag = {"red": 12, "green": 13, "blue": 14}

rex = re.compile("Game\s(?P<game_id>\d+): ")
colors_rex = re.compile("(?P<n>[0-9]+)\s(?P<color>[a-z]+)")

powers = []


with open("../../puzzles/2.txt") as f:
    for l in f:
        game_id = rex.findall(l)[0]
        tirages = colors_rex.findall(l)

        maxes = {}

        for value, color in tirages:
            value = int(value)
            try:
                maxes[color] = value if value > maxes[color] else maxes[color]
            except KeyError:
                maxes[color] = value

        power = reduce(lambda x, y: x*y, maxes.values())
        powers.append(power)

    print(sum(powers))
