from collections import defaultdict

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2
HALT = 99

class IntcodeComputer:
    def __init__(self, inp_file, initial_address=None):
        f = list(map(int, open('input', 'r').read().split(',')))
        self.prog = defaultdict(int, enumerate(f))
        self.ptr = 0
        self.rel_ptr = 0
        self.modes = []
        self.outputs = []
        if initial_address is not None:
            self.prog[0] = initial_address

    def fetch_outputs(self):
        return self.outputs

    def process_instruction(self):
        op = self.prog[self.ptr]
        opcode = int(op % 100) # convert 02 to 2
        mode1 = int(op % 1_000 / 100)
        mode2 = int(op % 10_000 / 1_000)
        mode3 = int(op % 100_000 / 10_000)
        return opcode, mode1, mode2, mode3

    def read(self, offset):
        mode = self.modes[offset - 1]
        if mode == POSITION_MODE:
            return self.prog[self.prog[self.ptr + offset]]
        elif mode == IMMEDIATE_MODE:
            return self.prog[self.ptr + offset]
        elif mode == RELATIVE_MODE:
            new_ptr = self.prog[self.ptr + offset] + self.rel_ptr
            return self.prog[new_ptr]

    def write(self, val, offset):
        mode = self.modes[offset - 1]
        if mode == POSITION_MODE:
            self.prog[self.prog[self.ptr + offset]] = val
        elif mode == RELATIVE_MODE:
            rel_addr = self.prog[self.ptr + offset] + self.rel_ptr
            self.prog[rel_addr] = val

    def run(self, input_no):
        self.outputs = []
        processed_input = False
        while self.prog[self.ptr] != HALT:
            opcode, *self.modes = self.process_instruction()
            param1, param2 = self.read(1), self.read(2)
            if opcode == 1:
                self.write(param1 + param2, 3)
                self.ptr += 4
            elif opcode == 2:
                self.write(param1 * param2, 3)
                self.ptr += 4
            elif opcode == 3:
                if processed_input:
                    break
                self.write(input_no, 1)
                processed_input = True
                self.ptr += 2
            elif opcode == 4:
                #print(param1)
                self.outputs.append(param1)
                self.ptr += 2
            elif opcode == 5:
                self.ptr = self.ptr + 3 if param1 == 0 else param2
            elif opcode == 6:
                self.ptr = param2 if param1 == 0 else self.ptr + 3
            elif opcode == 7:
                self.write(int(param1 < param2), 3)
                self.ptr += 4
            elif opcode == 8:
                self.write(int(param1 == param2), 3)
                self.ptr += 4
            elif opcode == 9:
                self.rel_ptr += param1
                self.ptr += 2

