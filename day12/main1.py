import re
from itertools import combinations
from collections import defaultdict
from math import gcd

velocities = defaultdict(lambda : {'x': 0, 'y':0, 'z': 0})
moons = {}

for index, line in enumerate(open('input', 'r').readlines()):
    moon = line.rstrip()
    result = re.search(r'<x=(.*?), y=(.*?), z=(.*?)>', moon)
    x, y, z = map(int, result.groups())
    moons[index] = (int(x), int(y), int(z))

def update_velocity(v1, v2, axes, moon1, moon2):
    if v2 > v1:
        velocities[moon1][axes] += 1
        velocities[moon2][axes] -= 1
    elif v1 > v2:
        velocities[moon2][axes] += 1
        velocities[moon1][axes] -= 1

def is_cyclic(vals):
    l = len(vals)
    return False if l % 2 != 0 else vals[0:l//2] == vals[l//2:]


def lcm(a, b, c):
    lcm1 = int(a * b / gcd(a,b))
    return int(c * lcm1 / gcd(c, lcm1))


found_x = False
found_y = False
found_z = False

final_x = 0
final_y = 0
final_z = 0

step = 0

xs = []
ys = []
zs = []

while True:
    for (moon1, c1), (moon2, c2) in list(combinations(enumerate(moons.values()), 2)):
        x1, x2 = c1[0], c2[0]
        y1, y2 = c1[1], c2[1]
        z1, z2 = c1[2], c2[2]
        
        update_velocity(x1, x2, 'x', moon1, moon2)
        update_velocity(y1, y2, 'y', moon1, moon2)
        update_velocity(z1, z2, 'z', moon1, moon2)

    x_state = []
    y_state = []
    z_state = []
    for index, moon in moons.items():
        x, y, z = moon
        # update moon positions
        moons[index] = (velocities[index]['x'] + x,
                        velocities[index]['y'] + y,
                        velocities[index]['z'] + z)
        x_state.append(x)
        y_state.append(y)
        z_state.append(z)

    xs.append(tuple(x_state))
    ys.append(tuple(y_state))
    zs.append(tuple(z_state))

    if not found_x and is_cyclic(xs):
        final_x = step + 1
        print(f'X CYCLIC OVER {final_x}')
        found_x = True
        #xs = []

    if not found_y and is_cyclic(ys):
        final_y = step + 1
        print(f'Y CYCLIC OVER {final_y}')
        found_y = True
        #ys = []

    if not found_z and is_cyclic(zs):
        final_z = step + 1
        print(f'Z CYCLIC OVER {final_z}')
        found_z = True
        #zs = []

    if found_x and found_y and found_z:
        print(final_x, final_y, final_z)
        # counted steps twice!
        print(f'LCM is {lcm(final_x, final_y, final_z) / 2}')
        break

    step += 1

"""
energy = 0
for index, moon in moons.items():
    potential_energy = abs(moon[0]) + abs(moon[1]) + abs(moon[2])
    kinetic_energy = 0
    for val in velocities[index].values():
        kinetic_energy += abs(val)

    energy += (potential_energy * kinetic_energy)
print(energy)
"""
