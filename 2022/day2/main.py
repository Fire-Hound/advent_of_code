with open("input.txt") as f:
    games = f.read().splitlines()

def part1():
    total = 0
    for game in games:
        game = game.split(" ")
        score = 0
        if game[1] == 'X':
            score += 1
            if game[0] == 'A':
                score += 3
            elif game[0] == 'C':
                score += 6
        elif game[1] == 'Y':
            score += 2
            if game[0] == 'B':
                score += 3
            elif game[0] == 'A':
                score += 6
        elif game[1] == 'Z':
            score += 3
            if game[0] == 'C':
                score += 3
            elif game[0] == 'B':
                score += 6
        total += score

    print(total)

def part2():
    total = 0
    for game in games:
        game = game.split(" ")
        score = 0
        if game[1] == 'X':
            score += 0
            if game[0] == 'A':
                score += 3
            elif game[0] == 'B':
                score += 1
            elif game[0] == 'C':
                score += 2
        elif game[1] == 'Y':
            score += 3
            if game[0] == 'A':
                score += 1
            elif game[0] == 'B':
                score += 2
            elif game[0] == 'C':
                score += 3
        elif game[1] == 'Z':
            score += 6
            if game[0] == 'A':
                score += 2
            elif game[0] == 'B':
                score += 3
            elif game[0] == 'C':
                score += 1
        total += score

    print(total)

if __name__ == "__main__":
    part2()