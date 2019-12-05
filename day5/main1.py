def process_op(op):
    opcode = int(op % 100) # convert 02 to 2
    mode1 = int(op % 1_000 / 100)
    mode2 = int(op % 10_000 / 1_000)
    mode3 = int(op % 100_000 / 10_000)
    return opcode, mode1, mode2, mode3

with open('input', 'r') as f:
    position = 0
    inp = 1
    p = list(map(int, f.read().split(',')))

    while True:
        opcode, mode1, mode2, mode3 = process_op(p[position])
        if opcode == 1 or opcode == 2:
            param1 = p[p[position + 1]] if not mode1 else p[position + 1]
            param2 = p[p[position + 2]] if not mode2 else p[position + 2]
            p[p[position + 3]] = param1 + param2 if opcode == 1 else param1 * param2
            position +=4
        elif opcode == 3:
            addr = p[position + 1] if not mode1 else position + 1
            p[addr] = inp
            position += 2
        elif opcode == 4:
            addr = p[position + 1] if not mode1 else position + 1
            print(p[addr])
            position += 2
        else:
            break # opcode is 99 

