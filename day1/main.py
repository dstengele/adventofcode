def part1(input_list):
        for number1 in input_list:
            input_list = input_list[1:]
            for number2 in input_list:
                print(f"[PART 1] Checking {number1}+{number2}")
                if number1 + number2 == 2020:
                    print(f"[PART 1] Result found: Number 1: {number1}, Number 2: {number2}, Final Result: {number1 * number2}")
                    return number1 * number2


def part2(input_list):
    for number1 in input_list:
        input_list = input_list[1:]
        for number2 in input_list[1:]:
            for number3 in input_list[2:]:
                print(f"[PART 2] Checking {number1}+{number2}+{number3}")
                if number1 + number2 + number3 == 2020:
                    print(f"[PART 2] Result found: Number 1: {number1}, Number 2: {number2}, Number 3: {number3}, Final Result: {number1 * number2 * number3}")
                    return number1 * number2 * number3


if __name__ == '__main__':
    with open("input.txt", "r") as input_file:
        input_list = [int(number) for number in input_file.readlines()]
        part1(input_list)
        part2(input_list)