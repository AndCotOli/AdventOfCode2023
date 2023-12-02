"""Solutions for day 1 of advent of code 2023."""

import regex as re


def part1(filename: str = "../Input/day1.test") -> int:
    """Solution for part 1."""
    numregex = re.compile(r"[0-9]")
    with open(filename) as file:
        input = file.read().strip().split("\n")
        return sum(
            int(n[0]) * 10 + int(n[-1])
            for n in (numregex.findall(line) for line in input)
        )


def part2(filename: str = "../Input/day1-2.test") -> int:
    """Solution for part 2."""
    numbers = (
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    numregex = re.compile("[0-9]|" + "|".join(numbers))

    def toNum(string: str) -> int:
        return numbers.index(string) + 1 if string in numbers else int(string)

    with open(filename) as file:
        input = file.read().strip().split("\n")
        return sum(
            toNum(n[0]) * 10 + toNum(n[-1])
            for n in (numregex.findall(line, overlapped=True) for line in input)
        )


if __name__ == "__main__":
    input = "../Input/day1"
    print(f"Solution for part 1 is {part1(input)}")
    print(f"Solution for part 2 is {part2(input)}")
