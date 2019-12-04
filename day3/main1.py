import os

_x = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
_y = {'U': 1, 'D': -1, 'L': 0, 'R': 0}

def get_points(wire):
    points = set()
    x = y = 0
    for move in wire:
        direction = move[0]
        amount = int(move[1:])
        for _ in range(amount):
            x += _x[direction]
            y += _y[direction]
            points.add((x,y))

    return points

with open('input', 'r') as f:
    wires = f.read().splitlines()
    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')

    points1 = get_points(wire1)
    points2 = get_points(wire2)
    intersections = points1.intersection(points2)

    result = min(abs(p[0]) + abs(p[1]) for p in intersections)
    print(result)




