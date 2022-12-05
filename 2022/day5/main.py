import re


class Stack:
    def __init__(self, name, crates=None):
        self.name = name
        self.crates = [] if crates is None else crates

    def parse_stack(self, stack_str):
        self.crates = [int(crate) for crate in stack_str.split("\n")]

    def push(self, crate):
        self.crates.append(crate)

    def pop(self):
        return self.crates.pop()

    def __str__(self):
        return f"Stack {self.name}: {self.crates}"

    def __repr__(self):
        return str(self.crates)


class Stacks:
    def parse(self, stacks_str):
        stacks = {}
        stack_rows = stacks_str.split("\n")
        for i, name in enumerate(stack_rows[-1][1::4]):
            stacks[name] = Stack(
                name=name, crates=[])
        for stack_row in stack_rows[:-1]:
            for i, crate in enumerate(stack_row[1::4]):
                name = stack_rows[-1][1::4][i]
                if crate == " ":
                    continue
                stacks[name].crates.insert(0, crate)
        print(stacks)
        self.stacks = stacks

    def parse_move_order(self, move_str):
        move = re.findall(r"\d+", move_str)
        move_order = {}
        move_order['move'] = move[0]
        move_order['_from'] = move[1]
        move_order['to'] = move[2]
        return move_order

    def move(self, move, _from, to, preserve_order=False):
        # print(f"Move {move} from {_from} to {to}")
        crates_to_move = []
        for _ in range(int(move)):
            crates_to_move.append(self.stacks[_from].pop())
        if preserve_order:
            crates_to_move = crates_to_move[::-1]
        for crate in crates_to_move:
            self.stacks[to].push(crate)


def part1():
    stacks = Stacks()
    stacks.parse(input_stacks)

    for move in moves.split("\n"):
        move_order = stacks.parse_move_order(move)
        stacks.move(**move_order)

    for stack in stacks.stacks.values():
        print(stack.crates[-1], end="")


def part2():
    stacks = Stacks()
    stacks.parse(input_stacks)
    for move in moves.split("\n"):
        # parse move order
        move_order = stacks.parse_move_order(move)
        stacks.move(**move_order, preserve_order=True)

    for stack in stacks.stacks.values():
        print(stack.crates[-1], end="")


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.read()
        input_stacks, moves = data.split("\n\n")
        part1()
        part2()
