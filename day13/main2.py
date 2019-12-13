from comp import IntcodeComputer
from time import sleep

# EMPTY, WALL, BLOCK, PADDLE, BALL
objects = {
    0: ' ',
    1: '|',
    2: 'B',
    3: '_',
    4: 'O',
}

coords = {}
comp = IntcodeComputer('input', initial_address=2)

max_x = max_y = score = 0
paddle_x = ball_x = None

while True:
    if paddle_x != None:
        if paddle_x == ball_x:
            comp.run(0)
        elif paddle_x < ball_x:
            comp.run(1)
        else:
            comp.run(-1)
    else:
        comp.run(1)

    outs = comp.fetch_outputs()
    if len(outs) == 0:
        break

    for i in range(0, len(outs), 3):
        x, y, t = outs[i:i+3]
        if t in objects:
            coords[(x,y)] = objects[t]
        else:
            score = t
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    grid = [[' '] * (max_x) for y in range(max_y)]

    for c, t in coords.items():
        x = c[0] - 1
        y = c[1] - 1
        grid[y][x] = t
        if t == 'O':
            ball_x = x
        elif t == '_':
            paddle_x = x

    print(f'Score: {score}')
    [print(''.join(l)) for l in grid]

