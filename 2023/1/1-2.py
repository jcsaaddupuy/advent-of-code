import re


rex = re.compile("[0-9]")


replacements={"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
rex_replace=re.compile("(%s)" % "|".join(map(re.escape, replacements.keys())))



with open("./input.txt") as f:
    for l in f:
        print(l, rex_replace.sub(lambda mo: replacements.get(mo.group()), l))
    f.seek(0)
    result = sum(map(lambda numbers: int(numbers[0]+numbers[-1]), map(rex.findall, map(lambda l: rex_replace.sub(lambda mo: replacements.get(mo.group(), mo.group()), l), f))))
print(result)