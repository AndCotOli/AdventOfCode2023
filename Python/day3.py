"""Solutions for advent of code day 3."""
import regex as re
from math import prod


def getChars(input):
    """Get symbols and adjacent numbers."""
    chars = {
        (r, c): []
        for r in range(len(input))
        for c in range(len(input[0]))
        if input[r][c] not in "0123456789."
    }

    for r, row in enumerate(input):
        for n in re.finditer(r"\d+", row):
            border = {
                (r, c)
                for r in (r - 1, r, r + 1)
                for c in range(n.start() - 1, n.end() + 1)
            }

            for o in border & chars.keys():
                chars[o].append(int(n.group()))

    return chars


def part1(filename: str = "../Input/day3.test") -> int:
    """Solution for part 1."""
    with open(filename) as file:
        input = file.read().strip().split("\n")

        chars = getChars(input)

        return sum(sum(p) for p in chars.values())


def part2(filename: str = "../Input/day3.test") -> int:
    """Solution for part 2."""
    with open(filename) as file:
        input = file.read().strip().split("\n")

        chars = getChars(input)

        return sum(prod(p) for p in chars.values() if len(p) == 2)


if __name__ == "__main__":
    input = "../Input/day3"
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
