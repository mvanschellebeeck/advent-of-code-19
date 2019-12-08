def process_op(op):
    opcode = int(op % 100) # convert 02 to 2
    mode1 = int(op % 1_000 / 100)
    mode2 = int(op % 10_000 / 1_000)
    return opcode, mode1, mode2


class Amplifier:
    def __init__(self, amplifier_id, phase):
        self.p = list(map(int, open('input', 'r').read().split(',')))
        self.id = amplifier_id
        self.position = 0
        self.phase = phase
        self.seen = False

    def run(self, inp):
        output = inp
        finish_combination = False
        while True:
            opcode, mode1, mode2 = process_op(self.p[self.position])
            if opcode == 1:
                self.p[self.p[self.position + 3]] = self.param(1, mode1) + self.param(2, mode2)
                self.position += 4
            elif opcode == 2:
                self.p[self.p[self.position + 3]] = self.param(1, mode1) * self.param(2, mode2)
                self.position += 4
            elif opcode == 3:
                addr = self.p[self.position + 1]
                if not self.seen:
                    self.p[addr] = int(self.phase)
                    self.seen = True
                else:
                    self.p[addr] = inp
                self.position += 2
            elif opcode == 4:
                output = self.p[self.p[self.position + 1]]
                self.position += 2
                break
            elif opcode == 5:
                self.position = self.position + 3 if self.param(1, mode1) == 0 else self.param(2, mode2)
            elif opcode == 6:
                self.position = self.param(2, mode2) if self.param(1, mode1) == 0 else self.position + 3
            elif opcode == 7:
                self.p[self.p[self.position + 3]] = 1 if self.param(1, mode1) < self.param(2, mode2) else 0
                self.position += 4
            elif opcode == 8:
                self.p[self.p[self.position + 3]] = 1 if self.param(1, mode1) == self.param(2, mode2) else 0
                self.position += 4
            elif opcode == 99:
                if self.id == 4:
                    finish_combination = True
                break # opcode is 99
            else:
                raise ValueError(f'opcode {opcode} as part of full instruction {self.p[self.position]} is not valid')

        return output, finish_combination

    def param(self, n, mode):
        return self.p[self.p[self.position + n]] if not mode else self.p[self.position + n]

from itertools import permutations, cycle

phases = permutations('56789', 5)
best_signal = 0

for index, phase in enumerate(phases):
    inp = 0
    amplifiers = [Amplifier(i, phase[i]) for i in range(5)]
    
    for amplifier in cycle(amplifiers):
        inp, finish_combination = amplifier.run(inp)
        if finish_combination:
            break

    best_signal = max(best_signal, inp) 

print(best_signal)
