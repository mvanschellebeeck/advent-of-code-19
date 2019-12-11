from math import atan2, degrees, sqrt


def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def convert(deg):
    if -90 <= deg <= 180:
        return deg + 90
    else:
        return deg + 450

def take_closest_asteroid(r, x, y, x_m, y_m):
    old_x, old_y = g[r]
    if dist(x, y, x_m, y_m) < dist(old_x, old_y, x_m, y_m):
        return (x,y)
    else:
        return (old_x, old_y)


def find_asteroids(x_m, y_m):
    res = set()
    for x in range(columns):
        for y in range(rows):
            if f[y][x] == '#' and (x, y) != (x_m, y_m):
                r = convert(degrees(atan2(y - y_m , x - x_m)))
                res.add(r)
                if r in g:
                    g[r] = take_closest_asteroid(r, x, y, x_m, y_m)
                else:
                    g[r] = (x,y)
    return sorted(res)

def remove_asteroids(angles):
    for angle in angles:
        x, y = g[angle]
        f[y][x] = '.'

f = [list(line.rstrip()) for line in open('input', 'r').readlines()]
rows = len(f)
columns = len(f[0])
g = {}

monitor_x = 26
monitor_y = 29

asteroid_angles = find_asteroids(monitor_x, monitor_y)

count = 200
i = 0
while True:
    i += 1
    if len(asteroid_angles) > count:
        result = asteroid_angles[count - 1]
        x, y = g[result]
        print(100 * x + y)
        break
    else:
        print(f'rotation {i}')
        count -= len(asteroid_angles)
        remove_asteroids(asteroid_angles)
        asteroid_angles = find_asteroids(monitor_x, monitor_y)

