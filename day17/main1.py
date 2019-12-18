from comp import IntcodeComputer

c = IntcodeComputer('input')
c.run(1)
outs = c.fetch_outputs()
formatted_outs = list(map(lambda x: str(chr(x)), outs))


print(''.join(formatted_outs))

outs = list(filter(lambda x: x != 10, outs))
grid = [outs[i:i+39] for i in range(0, len(outs), 39)]
columns = len(grid[0])
rows = len(grid)

def is_intersection(c, r):
    if c in (0, columns - 1) or r in (0, rows - 1):
        return False
    if grid[r][c-1] == 35 and grid[r][c+1] == 35 and grid[r-1][c] == 35 and grid[r+1][c] == 35:
        return True

result = []
for r in range(rows):
    for c in range(columns):
        if grid[r][c] == 35 and is_intersection(c, r):
            result.append((c,r))

answer = 0
for i in result:
    answer += i[0] * i[1]

print(result)
print(answer)
