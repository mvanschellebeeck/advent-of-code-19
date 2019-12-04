lower = 359282
higher = 820401
count = 0

def has_double_not_in_group(s):
    prev_num = None
    flag = False
    counter = 1
    for num in s:
        if num == prev_num:
            counter += 1
            if counter < 3:
                flag = True
            else:
                flag = False
        elif counter == 2:
            return True
        else:
            counter = 1
        prev_num = num

    return flag

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
    if not has_double_not_in_group(s) or not increasing(s):
        continue
    count += 1

print(count)
