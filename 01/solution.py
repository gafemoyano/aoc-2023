from pathlib import Path
import re

path = Path(__file__).parent / "input.txt"
input = open(path, "r")

test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".splitlines()


number_regex = re.compile("(?=(\d|one|two|three|four|five|six|seven|eight|nine))")


def string_to_number(string_number):
    match string_number:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return string_number


calibrations = []

for line in input:
    chars = list(line)
    reversed_chars = list(reversed(chars))
    matches = number_regex.findall(line)
    first = string_to_number(matches[0])
    last = string_to_number(matches[-1])

    print(line, matches, "\n")

    calibrations.append(int(first + last))


print(sum(calibrations))
