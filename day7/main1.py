def process_op(op):
    opcode = int(op % 100) # convert 02 to 2
    mode1 = int(op % 1_000 / 100)
    mode2 = int(op % 10_000 / 1_000)
    mode3 = int(op % 100_000 / 10_000)
    return opcode, mode1, mode2, mode3


from itertools import permutations

phases = permutations('01234', 5)
best_signal = 0

for index, phase in enumerate(phases):
    prev = 0
    for amplifier in range(0,5):
        def param(n, mode):
            return p[p[position + n]] if not mode else p[position + n]

        p = list(map(int, open('input', 'r').read().split(',')))
        position = 0
        amplifier_no = int(phase[amplifier])
        seen = False
        while True:
            opcode, mode1, mode2, mode3 = process_op(p[position])
            if opcode == 1:
                p[p[position + 3]] = param(1, mode1) + param(2, mode2)
                position += 4
            elif opcode == 2:
                p[p[position + 3]] = param(1, mode1) * param(2, mode2)
                position += 4
            elif opcode == 3:
                addr = p[position + 1]
                if not seen:
                    p[addr] = amplifier_no
                    seen = True
                else:
                    p[addr] =  prev
                position += 2
            elif opcode == 4:
                prev = p[p[position + 1]]
                position += 2
                if amplifier == 4:
                    best_signal = max(best_signal, prev)
            elif opcode == 5:
                position = position + 3 if param(1, mode1) == 0 else param(2, mode2)
            elif opcode == 6:
                position = param(2, mode2) if param(1, mode1) == 0 else position + 3
            elif opcode == 7:
                p[p[position + 3]] = 1 if param(1, mode1) < param(2, mode2) else 0
                position += 4
            elif opcode == 8:
                p[p[position + 3]] = 1 if param(1, mode1) == param(2, mode2) else 0
                position += 4
            else:
                break # opcode is 99

print(best_signal)
