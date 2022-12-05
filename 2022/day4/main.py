def get_sections(pair):
    elf1_section, elf2_section = pair.split(",")

    elf1_section = [int(section)
                    for section in elf1_section.split("-")]
    elf1_section = list(
        range(elf1_section[0], elf1_section[1] + 1))

    elf2_section = [int(section)
                    for section in elf2_section.split("-")]
    elf2_section = list(
        range(elf2_section[0], elf2_section[1] + 1))

    return elf1_section, elf2_section


def part1():
    total = 0
    for pair in pairs:
        elf1_section, elf2_section = get_sections(pair)

        union = set(elf1_section).union(set(elf2_section))
        if len(union) == len(elf1_section) or len(union) == len(elf2_section):
            total += 1
    print(total)


def part2():
    total = 0
    for pair in pairs:
        elf1_section, elf2_section = get_sections(pair)

        intersection = set(elf1_section).intersection(set(elf2_section))
        if len(intersection) > 0:
            total += 1
    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        pairs = f.read().split("\n")

    part1()
    part2()
