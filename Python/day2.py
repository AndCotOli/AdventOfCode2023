"""Solutions for advent of code day 2."""
import regex as re


def part1(filename: str = "../Input/day2.test") -> int:
    """Solution for part 1."""
    maxCubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    sol = 0

    regexp = re.compile(r"(\d+) (\w+)")
    with open(filename) as file:
        input = file.read().strip().split("\n")

        game = 1
        for line in input:
            valid = True
            draws = regexp.findall(line)
            for draw in draws:
                if int(draw[0]) > maxCubes[draw[1]]:
                    valid = False
                    break
            if valid:
                sol += game

            game += 1

    return sol


def part2(filename: str = "../Input/day2-2.test") -> int:
    """Solution for part 2."""
    regexp = re.compile(r"(\d+) (\w+)")

    def maxCubes(color: str, draws) -> int:
        return int(max(draws, key=lambda k: int(k[0]) if k[1] == color else 0)[0])

    with open(filename) as file:
        input = file.read().strip().split("\n")

        return sum(
            maxCubes("red", draws) * maxCubes("green", draws) * maxCubes("blue", draws)
            for draws in (regexp.findall(line) for line in input)
        )


if __name__ == "__main__":
    input = "../Input/day2"
    print(f"Solution for part 1 is: {part1(input)}")
    print(f"Solution for part 2 is: {part2(input)}")
