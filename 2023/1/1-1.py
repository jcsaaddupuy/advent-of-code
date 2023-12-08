import re


rex = re.compile("[0-9]")

with open("./input.txt") as f:
    result = sum(map(lambda numbers: int(numbers[0]+numbers[-1]), map(rex.findall, f)))
print(result)