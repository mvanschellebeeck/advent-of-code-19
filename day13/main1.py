from comp import IntcodeComputer
from functools import reduce

# EMPTY, WALL, BLOCK, PADDLE, BALL
objects = [' ', 'W', 'B','P', 'O']
coords = {}

def count_tiles(t):
    return list(coords.values()).count(t)

c = IntcodeComputer('input')

while True:
    c.run(1)
    outs = c.fetch_outputs()
    if len(outs) == 0:
        break

    for i in range(0, len(outs), 3):
        x, y, t = outs[i:i+3]
        coords[(x,y)] = objects[t]

print(count_tiles('B'))

