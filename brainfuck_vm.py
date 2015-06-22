from time import sleep

#Simple brainfuck interpreter
def load_program(file_name):
    infile = open(file_name, 'r')
    program_str = ""
    for line in infile:
        program_str = program_str + line
    program = []
    for c in program_str:
        if c in ['<','>','-','+','[',']',',','.']:
            program.append(c)
    return program

class brainfuck_vm:
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.memory = {}
        self.p = 0
        self.memory[self.p] = 0
        self.loop_stack = []
    def step(self):
        if len(self.program) <= self.pc:
            return False
        instruction = self.program[self.pc]
        if instruction == '<':
            self.p = self.p - 1
            if not self.p in self.memory:
                self.memory[self.p] = 0
        if instruction == '>':
            self.p = self.p + 1
            if not self.p in self.memory:
                self.memory[self.p] = 0
        if instruction == '-':
                if self.memory[self.p] == 0:
                    self.memory[self.p] = 255
                else:
                    self.memory[self.p] = self.memory[self.p] - 1
        if instruction == '+':
            self.memory[self.p] = (self.memory[self.p] + 1) % 255
        if instruction == '.':
            print(chr(self.memory[self.p]), end='')
        if instruction == ',':
            self.memory[self.p] = ord(raw_input("> ")[0])
        if instruction == '[':
            self.loop_stack.append(self.pc + 1)
        if instruction == ']':
            if self.memory[self.p] == 0:
                self.loop_stack.pop()
            else:
                self.pc = self.loop_stack[-1] - 1
        self.pc = self.pc + 1
        return True
    def dumpState(self):
        for k, v in self.memory.items():
            print(v, end=' ')
        print("")
        print("PC: " + str(self.pc) + ", P: " + str(self.p) + ", Stack: " + str(self.loop_stack))

prog = load_program("programs/hello.bf")
print(prog)

vm = brainfuck_vm(prog)
while True:
    #vm.dumpState()
    #sleep(1)
    if not vm.step():
        break

print("\nProgram ended")
