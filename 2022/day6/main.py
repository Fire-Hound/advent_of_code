def is_start_sequence(string):
    return len(string) == len(set(string))


def part1():
    for i, _ in enumerate(buffer[4:], 4):
        if is_start_sequence(buffer[i-4:i]):
            return i


def part2():
    for i, _ in enumerate(buffer[14:], 14):
        if is_start_sequence(buffer[i-14:i]):
            return i


if __name__ == "__main__":
    with open("input.txt") as f:
        buffer = f.read()
    print(part1())
    print(part2())
