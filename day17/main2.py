from comp import IntcodeComputer

def print_grid(outs):
    formatted_outs = list(map(lambda x: str(chr(x)), outs))
    print(''.join(formatted_outs))

c = IntcodeComputer('input')
c.run(1)
outs = c.fetch_outputs()
#print_grid(outs)


outs = list(filter(lambda x: x != 10, outs))
grid = [outs[i:i+39] for i in range(0, len(outs), 39)]
columns = len(grid[0])
rows = len(grid)

def is_intersection(c, r):
    if c in (0, columns - 1) or r in (0, rows - 1):
        return False
    if grid[r][c-1] == 35 and grid[r][c+1] == 35 and grid[r-1][c] == 35 and grid[r+1][c] == 35:
        return True

intersections = []
scaffolding = set()
robot = None

for r in range(rows):
    for c in range(columns):
        if grid[r][c] == ord('#'):
            scaffolding.add((r,c))
            if is_intersection(c, r):
                intersections.append((c,r))
        elif grid[r][c] == ord('^'):
            robot = (r, c)


c2 = IntcodeComputer('input', initial_address=2)

def run_command(chars):
    for c in chars:
        c2.run(ord(c))

    c2.run(ord('\n'))

# A
# L4 
# L6
# L8
# L12

# B
# L8
# R12
# L12

# B
# L8
# R12
# L12

# A
# L4
# L6
# L8
# L12

# B
# L8
# R12
# L12

# C
# R12
# L6 
# L6
# L8

# A
# L4
# L6 
# L8
# L12 

# C
# R12
# L6
# L6
# L8

# B
# L8
# R12
# L12

# C
# R12
# L6
# L6
# L8


run_command('A,B,B,A,B,C,A,C,B,C')
run_command('L,4,L,6,L,8,L,12')
run_command('L,8,R,12,L,12')
run_command('R,12,L,6,L,6,L,8')
run_command('n')

outs = c2.fetch_outputs()
#print_grid(outs)
print(outs[-1])

