# Write a program that will receive various brainf*** programs as arguments and execute each program in turn.

import sys

def execute(program: str):
    tape = [0] * 30000
    head = 0
    str_pointer = 0
    program_length = len(program)
    loop_stack = []

    while str_pointer < program_length:
        char = program[str_pointer]

        if char == '.':
            print(chr(tape[head]), end='')
        elif char == '+':
            tape[head] = (tape[head] + 1) % 256
        elif char == '-':
            tape[head] = (tape[head] - 1) % 256
        elif char == '>':
            head += 1
            if head >= len(tape):
                head = 0  # Wrap around to the beginning
        elif char == '<':
            head -= 1
            if head < 0:
                head = len(tape) - 1  # Wrap around to the end
        elif char == '[':
            if tape[head] == 0:
                # Jump to the matching ']'
                open_brackets = 1
                while open_brackets != 0:
                    str_pointer += 1
                    if program[str_pointer] == '[':
                        open_brackets += 1
                    elif program[str_pointer] == ']':
                        open_brackets -= 1
            else:
                # Add current position to loop stack
                loop_stack.append(str_pointer)
        elif char == ']':
            if tape[head] != 0:
                # Jump back to the matching '['
                str_pointer = loop_stack[-1]
            else:
                # Pop from loop stack
                loop_stack.pop()

        str_pointer += 1


def main():
    for arg in sys.argv[1:]:
        execute(arg)

if __name__ == "__main__":
    main()
