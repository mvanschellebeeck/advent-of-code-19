
lower = 359282
higher = 820401
count = 0

def has_double(s):
    prev_num = None
    for num in s:
        if num == prev_num:
            return True
        else:
            prev_num = num
    return False

def increasing(s):
    prev_num = 0
    for num in s:
        num = int(num)
        if num < prev_num:
            return False
        else:
            prev_num = num

    return True

for i in range(lower, higher + 1):
    s = str(i)
    if not has_double(s) or not increasing(s):
        continue
    count += 1

print(count)
