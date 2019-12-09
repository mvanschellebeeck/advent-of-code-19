from collections import defaultdict

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2
HALT = 99

class IntcodeComputer:
    def __init__(self, inp_file):
        f = list(map(int, open('input', 'r').read().split(',')))
        self.prog = defaultdict(int, enumerate(f))
        self.ptr = 0
        self.rel_ptr = 0

    def process_instruction(self):
        op = self.prog[self.ptr]
        opcode = int(op % 100) # convert 02 to 2
        mode1 = int(op % 1_000 / 100)
        mode2 = int(op % 10_000 / 1_000)
        mode3 = int(op % 100_000 / 10_000)
        return opcode, mode1, mode2, mode3

    def read(self, offset, mode):
        if mode == POSITION_MODE:
            return self.prog[self.prog[self.ptr + offset]]
        elif mode == IMMEDIATE_MODE:
            return self.prog[self.ptr + offset]
        elif mode == RELATIVE_MODE:
            new_ptr = self.prog[self.ptr + offset] + self.rel_ptr
            return self.prog[new_ptr]

    def write(self, val, offset, mode):
        if mode == POSITION_MODE:
            self.prog[self.prog[self.ptr + offset]] = val
        elif mode == RELATIVE_MODE:
            rel_addr = self.prog[self.ptr + offset] + self.rel_ptr
            self.prog[rel_addr] = val

    def fetch_params(self, mode1, mode2):
        return self.read(1, mode1), self.read(2, mode2)

    def run(self, input_no):
        while self.prog[self.ptr] != HALT:
            opcode, mode1, mode2, mode3 = self.process_instruction() # rename process_instruction
            param1, param2 = self.fetch_params(mode1, mode2)
            if opcode == 1:
                self.write(param1 + param2, 3, mode3)
                self.ptr += 4
            elif opcode == 2:
                self.write(param1 * param2, 3, mode3)
                self.ptr += 4
            elif opcode == 3:
                self.write(input_no, 1, mode1)
                self.ptr += 2
            elif opcode == 4:
                print(param1)
                self.ptr += 2
            elif opcode == 5:
                self.ptr = self.ptr + 3 if param1 == 0 else param2
            elif opcode == 6:
                self.ptr = param2 if param1 == 0 else self.ptr + 3
            elif opcode == 7:
                self.write(int(param1 < param2), 3, mode3)
                self.ptr += 4
            elif opcode == 8:
                self.write(int(param1 == param2), 3, mode3)
                self.ptr += 4
            elif opcode == 9:
                self.rel_ptr += param1
                self.ptr += 2

p1 = 1
p2 = 2
comp = IntcodeComputer('input')
comp.run(p2)
