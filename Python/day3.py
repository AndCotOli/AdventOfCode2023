"""Solutions for advent of code day 3."""


def part1(filename: str = "../Input/day3.test") -> int:
    """Solution for part 1."""

    def isValidSymbol(char: str) -> bool:
        return char != "." and not char.isdigit()

    def checkSurroundings(index: tuple, input) -> bool:
        i, j = index
        up = max(i - 1, 0)
        left = max(j - 1, 0)
        right = min(j + 1, len(input[i]) - 1)
        down = min(i + 1, len(input) - 1)

        return (
            isValidSymbol(input[up][left])
            or isValidSymbol(input[up][j])
            or isValidSymbol(input[up][right])
            or isValidSymbol(input[i][left])
            or isValidSymbol(input[i][j])
            or isValidSymbol(input[i][right])
            or isValidSymbol(input[down][left])
            or isValidSymbol(input[down][j])
            or isValidSymbol(input[down][right])
        )

    def findNextSymbol(start: int, line: str) -> int:
        i = start
        while i < len(line):
            if not line[i].isdigit():
                return i
            i += 1
        return i

    sol = 0

    with open(filename) as file:
        input = file.read().strip().split("\n")
        i = 0
        while i < len(input):
            line = input[i]
            j = 0
            while j < len(line):
                if line[j].isdigit():
                    lastDigit = findNextSymbol(j, line) - 1
                    if checkSurroundings((i, j), input) or checkSurroundings(
                        (i, lastDigit), input
                    ):
                        sol += int(line[j : lastDigit + 1])
                        j = lastDigit
                j += 1
            i += 1

        return sol


def part2(filename: str = "../Input/day3.test") -> int:
    """Solution for part 2."""
    pass


if __name__ == "__main__":
    input = "../Input/day3"
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")
