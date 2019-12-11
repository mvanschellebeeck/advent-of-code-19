from comp import IntcodeComputer
from math import inf
from collections import defaultdict

c = IntcodeComputer('input')

LR = { 0: 'L', 1: 'R'}
move = {
    'U': { 'L' : (-1, 0, 'L'), 'R': (1, 0, 'R') },
    'D': { 'L': (1, 0, 'R'), 'R': (-1, 0, 'L') },
    'L': { 'L': (0, -1, 'D'), 'R': (0, 1, 'U') },
    'R': { 'L': (0, 1, 'U'), 'R': (0, -1, 'D') }
}


positions = defaultdict(int)
# position -> colour
positions[(0,0)] = 1
x = y = 0
pose = 'U'

while True:
    # feed current panel colour of position (x,y)
    c.run(positions[(x,y)])
    outputs = c.fetch_outputs()
    if len(outputs) == 0:
        break
    new_colour, direction = outputs
    positions[(x,y)] = new_colour # doesnt paint last panel
    turn = LR[direction]
    dx, dy, pose = move[pose][turn]
    x += dx
    y += dy


print(len(positions) - 1)

min_x = inf
max_x = 0

min_x = min(x[0] for x in positions.keys())
max_x = max(x[0] for x in positions.keys())
min_y = min(x[1] for x in positions.keys())
max_y = max(x[1] for x in positions.keys())

print(min_x, max_x, min_y, max_y)

# grid  42 * 5
grid = [[ ' ' for _ in range(43)] for _ in range(6)]

for k in positions.keys():
    x, y = k
    y = abs(y)
    grid[y][x] = '#' if positions[k] == 1 else ' '

for l in grid:
    print(''.join(l))

