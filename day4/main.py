import math
import re
from collections import OrderedDict


def part1(passports):
    print(f"[PART 1] Valid Passports: {count_valid_passports_part1(passports)}")


def part2(field):
    print(f"[PART 2] Valid Passports: {count_valid_passports_part2(passports)}")


def read_input_file(filename):
    with open(filename, "r") as input_file:
        passports = []
        new_passport = {}
        for input_row in input_file.readlines():
            if input_row.strip():
                params = {
                    param.split(":")[0]: param.split(":")[1]
                    for param in input_row.strip().split(" ")
                }
                new_passport = {**new_passport, **params}
            else:
                passports.append(new_passport)
                new_passport = {}
        passports.append(new_passport)
    return passports


def count_valid_passports_part1(passports):
    valid_count = 0
    for passport in passports:
        attributes = passport.keys()
        if (
            "byr" in attributes
            and "iyr" in attributes
            and "eyr" in attributes
            and "hgt" in attributes
            and "hcl" in attributes
            and "ecl" in attributes
            and "pid" in attributes
        ):
            valid_count += 1
    return valid_count


def count_valid_passports_part2(passports):
    valid_count = 0
    for passport in passports:
        passport["cid"] = "0"
        passport = OrderedDict(sorted(passport.items()))
        attributes = passport.keys()
        if not (
            "byr" in attributes
            and "iyr" in attributes
            and "eyr" in attributes
            and "hgt" in attributes
            and "hcl" in attributes
            and "ecl" in attributes
            and "pid" in attributes
        ):
            continue
        # test byr
        if not 1920 <= int(passport["byr"]) <= 2002:
            continue
        # test iyr
        if not 2010 <= int(passport["iyr"]) <= 2020:
            continue
        # test eyr
        if not 2020 <= int(passport["eyr"]) <= 2030:
            continue
        # test hgt
        height: str = passport["hgt"]
        if height.endswith("cm"):
            height_number = int(height.removesuffix("cm"))
            if not 150 <= height_number <= 193:
                continue
        elif height.endswith("in"):
            height_number = int(height.removesuffix("in"))
            if not 59 <= height_number <= 76:
                continue
        else:
            continue
        # test hcl
        if not re.match("^#[0-9a-f]{6}$", passport["hcl"]):
            continue
        # test ecl
        eyecolor = passport["ecl"]
        if eyecolor not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        # test pid
        if not re.match("^[0-9]{9}$", passport["pid"]):
            continue

        print(f"VALID: {[field.rjust(10, ' ') for field in passport.values()]}")
        valid_count += 1

    return valid_count


def test1():
    test_passports = read_input_file("testinput1.txt")
    assert count_valid_passports_part1(test_passports) == 2


def test2():
    test_passports_valid = read_input_file("testinput2_valid.txt")
    test_passports_invalid = read_input_file("testinput2_invalid.txt")
    assert count_valid_passports_part2(test_passports_valid) == 4
    assert count_valid_passports_part2(test_passports_invalid) == 0


if __name__ == "__main__":
    test1()
    test2()

    passports = read_input_file("input.txt")
    part1(passports)
    part2(passports)
