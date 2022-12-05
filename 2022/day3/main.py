def to_priority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1


def part1():
    total = 0
    for rucksack in rucksacks:
        compartment_one = rucksack[:len(rucksack)//2]
        compartment_two = rucksack[len(rucksack)//2:]

        duplicates = set(compartment_one).intersection(set(compartment_two))
        for duplicate in duplicates:
            total += to_priority(duplicate)

    print(total)


def part2():
    total = 0
    while len(rucksacks) > 0:
        # assuming rucksacks are divisible by 3
        rucksack_one = rucksacks.pop(0)
        rucksack_two = rucksacks.pop(0)
        rucksack_three = rucksacks.pop(0)

        duplicates = set(rucksack_one).intersection(
            set(rucksack_two)).intersection(set(rucksack_three))
        # only one duplicate would be possible
        total += to_priority(duplicates.pop())

    print(total)


if __name__ == "__main__":
    with open("input.txt") as f:
        rucksacks = f.read().split("\n")

    part1()
    part2()
