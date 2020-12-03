import math


def get_increased_modulo_row(start, inc, limit):
    row = start
    while True:
        yield row
        row = (row + inc) % limit


def get_hit_trees_for_slope(field, row_inc, col_inc):
    trees_hit_count = 0
    col_generator = get_increased_modulo_row(0, col_inc, 31)
    for row in range(0, len(field), row_inc):
        col = col_generator.__next__()
        square = field[row][col]
        if square == "#":
            trees_hit_count += 1

    print(f"[Slope: {row_inc} down, {col_inc} right] Trees hit: {trees_hit_count}")
    return trees_hit_count


def part1(field):
    print(f"[PART 1] Trees hit: {get_hit_trees_for_slope(field, 1, 3)}")


def part2(field):
    slope_hit_count = [
        get_hit_trees_for_slope(field, 1, 1),
        get_hit_trees_for_slope(field, 1, 3),
        get_hit_trees_for_slope(field, 1, 5),
        get_hit_trees_for_slope(field, 1, 7),
        get_hit_trees_for_slope(field, 2, 1),
    ]
    print(f"[PART 2] Trees hit: {math.prod(slope_hit_count)}")


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        field = [[square for square in row] for row in input_file.readlines()]
        part1(field)
        part2(field)
