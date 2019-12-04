import os

_x = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
_y = {'U': 1, 'D': -1, 'L': 0, 'R': 0}

def wire_path(wire):
    points = set()
    x = y = 0
    steps = 0
    counter = {}
    for move in wire:
        direction = move[0]
        amount = int(move[1:])
        for _ in range(amount):
            x += _x[direction]
            y += _y[direction]
            steps += 1
            points.add((x,y))
            if (x,y) not in counter:
                counter[(x,y)] = steps

    return points, counter

with open('input', 'r') as f:
    wires = f.read().splitlines()
    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')

    points1, counter1 = wire_path(wire1)
    points2, counter2 = wire_path(wire2)
    intersections = points1.intersection(points2)

    result = min(counter1[p] + counter2[p] for p in intersections)
    print(result)




