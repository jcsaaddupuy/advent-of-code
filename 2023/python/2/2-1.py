import re

bag = {"red": 12, "green": 13, "blue": 14}

rex = re.compile("Game\s(?P<game_id>\d+): ")
colors_rex = re.compile("(?P<n>[0-9]+)\s(?P<color>[a-z]+)")

possibles = []

with open("../../puzzles/2.txt") as f:
    for l in f:
        game_id = rex.findall(l)[0]
        tirages = colors_rex.findall(l)
        sums = {}

        possible = True
        for value, color in tirages:
            value = int(value)
            if value > bag[color]:
                print(f"{game_id} : impossible because {color} {value} > {bag[color]}")
                possible = False
                break

        if possible:
            print(game_id, "possible")
            possibles.append(int(game_id))

    print(sum(possibles))
