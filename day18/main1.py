grid = [list(line.strip()) for line in open('input', 'r').readlines()]

#grid = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""
#print(grid)
#grid = [list(line.strip()) for line in grid.split('\n')]

rows = len(grid)
columns = len(grid[0])

start = None

doors = dict()
keys = dict()

for r in range(rows):
    for c in range(columns):
        item = grid[r][c]
        if item == '@':
            start = (r, c)
        elif item not in ('.', '#'):
            if item.isupper():
                doors[item] = (r, c)
            else:
                keys[item] = (r, c)

# dfs to explore doors blocking keys

visited = set()
path_to_key = {}
distances = {}

def dfs(pos, q, depth=0):
    r, c = pos
    item = grid[r][c]
    if (r,c) in visited:
        return None
    if item == '#':
        return None
    elif item != '.':
        if item.islower():
            distances[item] = depth
            path_to_key[item] = q
            q = []
        elif item != '@': # i.e. a door
            q.append(item)
    visited.add((r,c))

    dfs((r - 1, c), q, depth + 1)
    dfs((r + 1, c), q, depth + 1)
    dfs((r, c - 1), q, depth + 1)
    dfs((r, c + 1), q, depth + 1)

dfs(start, [])
#print(start)
#print(doors)
#print(keys)
#print(paths)

for key, doors in path_to_key.items():
    print(f'Distance to {key}: {distances[key]}')
    print(f'{key}: {doors}')


