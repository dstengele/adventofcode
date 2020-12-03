def part1(passwords):
    valid_passwords_count = 0
    for entry in passwords:
        print(f"[PART 1] Checking password {entry['password']}")
        charcount_min = int(entry["policy"].split(" ")[0].split("-")[0])
        charcount_max = int(entry["policy"].split(" ")[0].split("-")[1])
        char_to_count = entry["policy"].split(" ")[1]

        charcount_in_password = entry["password"].count(char_to_count)

        if charcount_in_password >= charcount_min and charcount_in_password <= charcount_max:
            valid_passwords_count += 1
    print(f"[PART 1] Number of valid passwords: {valid_passwords_count}")

def part2(passwords):
    valid_passwords_count = 0
    for entry in passwords:
        print(f"[PART 2] Checking password {entry['password']}")
        charindex_1 = int(entry["policy"].split(" ")[0].split("-")[0])
        charindex_2 = int(entry["policy"].split(" ")[0].split("-")[1])
        char_to_find = entry["policy"].split(" ")[1]

        password = entry["password"]

        pos1matches = password[charindex_1 - 1] == char_to_find
        pos2matches = password[charindex_2 - 1] == char_to_find
        if pos1matches ^ pos2matches:
            valid_passwords_count += 1
    print(f"[PART 2] Number of valid passwords: {valid_passwords_count}")


if __name__ == '__main__':
    with open("input.txt", "r") as input_file:
        input_list = [{'policy': entry.split(":")[0], 'password': entry.split(":")[1].strip()} for entry in input_file.readlines()]
        part1(input_list)
        part2(input_list)