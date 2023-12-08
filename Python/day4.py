"""Solutions for day 4."""


def getMatches(card: str) -> int:
    """Get the number of matches of a given card."""
    winning, numbers = card.split(": ")[1].split(" | ")

    # All numbers have (at a maximum) 2 digits
    w = [int(winning[i : i + 2]) for i in range(0, len(winning), 3)]
    n = [int(numbers[i : i + 2]) for i in range(0, len(numbers), 3)]

    return sum(w.count(i) for i in n)


def part1(filename: str = "../Input/day4.test") -> int:
    """Solution for part 1."""
    sol = 0

    with open(filename) as file:
        input = file.read().strip().split("\n")
        for card in input:
            matches = getMatches(card)
            sol += 0 if matches == 0 else 2 ** (matches - 1)

    return sol


def part2(filename: str = "../Input/day4.test") -> int:
    """Solution for part 2."""
    with open(filename) as file:
        input = file.read().strip().split("\n")
        cards = {i: 1 for i in range(len(input))}
        for idx, card in enumerate(input):
            numCards = cards[idx]

            matches = getMatches(card)

            for i in range(1, matches + 1):
                cards[idx + i] += numCards

        return sum(cards.values())


if __name__ == "__main__":
    input = "../Input/day4"
    print(f"Solution for part 1: {part1(input)}")
    print(f"Solution for part 2: {part2(input)}")
