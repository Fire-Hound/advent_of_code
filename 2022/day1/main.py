
with open("input.txt") as f:
    all_input = f.read()
    inputs = all_input.split("\n\n")

inputs = [_input.split("\n") for _input in inputs]

def part1():
    max_calories = 0

    for _input in inputs:
        _input = [int(calories) for calories in _input]
        calories = sum(_input)
        if calories > max_calories:
            max_calories = calories

    print(max_calories)

def part2():
    all_calories = []

    for _input in inputs:
        _input = [int(calories) for calories in _input]
        calories = sum(_input)
        all_calories.append(calories)

    max_calories = sum(sorted(all_calories, reverse=True)[0:3])
    print(max_calories)

if __name__ == "__main__":
    part2()
