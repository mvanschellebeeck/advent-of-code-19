from math import atan2, degrees

def find_asteroids(x_m, y_m):
    res = set()
    for x in range(columns):
        for y in range(rows):
            if f[y][x] == '#' and (x, y) != (x_m, y_m):
                r = atan2(y - y_m, x - x_m)
                res.add(r)
    return len(res)


f = [list(line.rstrip()) for line in open('input', 'r').readlines()]
rows = len(f)
columns = len(f[0])

best = None
best_count = 0

for x in range(columns):
    for y in range(rows):
        if f[y][x] == '#':
            count = find_asteroids(x, y)
            if count > best_count:
                best_count = count
                best = (x, y)

print(best, best_count)
