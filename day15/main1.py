from comp import IntcodeComputer
from collections import defaultdict
import random

WALL = 0
MOVE = 1
FOUND = 2

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

c = IntcodeComputer('input')
x = y = 0


grid = defaultdict(lambda x: ' ')
ds = set([NORTH, SOUTH, WEST, EAST])

def move(x, y, d):
    if d == NORTH:
        return (x, y + 1)
    elif d == SOUTH:
        return (x, y - 1)
    elif d == WEST:
        return (x - 1, y)
    elif d == EAST:
        return (x + 1, y)

class colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colour(s):
    if s == '-':
        return f'{colours.OKGREEN}{s}{colours.ENDC}'
    elif s == '#':
        return f'{colours.FAIL}{s}{colours.ENDC}'
    elif s == 'B':
        return f'{colours.WARNING}{s}{colours.ENDC}'
    elif s == 'O':
        return f'{colours.BOLD}{s}{colours.ENDC}'
    else:
        return ' '

def print_grid(grid):
    max_x = max(i[0] for i in grid.keys())
    max_y = max(i[1] for i in grid.keys())
    min_x= min(i[0] for i in grid.keys())
    min_y = min(i[1] for i in grid.keys())

    result = [[' ' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    for point, status in grid.items():
        x, y = point
        x += abs(min_x)
        y += abs(min_y)
        result[y][x] = colour(status)

    [print(''.join(l)) for l in result]


opposite = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST
}

q = defaultdict(lambda: set([NORTH, SOUTH, EAST, WEST]))

def is_dead_end(x, y):
    directions = set()
    for d in ds:
        m = move(x, y, d)
        if m in grid and (grid[m] in ('#', '-', 'O')):
            directions.add(d)
    return len(ds - directions) == 0


backtrack = []
complete = False
oxygen = (None, None)
answer = 0
while not complete:
    if (x,y) != oxygen:
        grid[(x,y)] = '-'

    # pick a possible direction and explore it
    if is_dead_end(x, y):
        while is_dead_end(x,y):
            if len(backtrack) == 0:
                complete = True
                break
            direction = backtrack.pop()
            c.run(direction)
            q[(x,y)] -= set([opposite[direction]])
            (x, y) = move(x, y, direction)
            answer -= 1
        continue
    else:
        direction = random.choice(list(q[(x,y)]))

    c.run(direction)
    status = c.fetch_outputs()[0]
    q[(x,y)] -= set([direction]) # mark direction as explored

    if status == WALL:
        grid[move(x, y, direction)] = '#'
    elif status == MOVE:
        backtrack.append(opposite[direction])
        (x, y) = move(x, y, direction)
        q[(x,y)] -= set([opposite[direction]])
        answer += 1
    elif status == FOUND:
        backtrack.append(opposite[direction])
        oxygen = (x,y) = move(x, y, direction)
        q[oxygen] -= set([opposite[direction]])
        grid[oxygen] = 'O'
        answer += 1
        print(f'Part 1: {answer}')

print_grid(grid)

# dfs to find max depth
complete = False
depth = 0
max_depth = 0
start = oxygen
explored = {}

def dfs(x, y, depth):
    explored[(x,y)] = depth
    for d in ds:
        new = move(x, y, d)
        if grid[new] != '#' and new not in explored:
            dfs(new[0], new[1], depth+1)
    return

dfs(start[0], start[1], 0)
print(f'Part 2: {max(explored.values())}')
