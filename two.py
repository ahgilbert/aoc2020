from os import path

if __name__ == '__main__':
    with open(path.join(path.dirname(__file__), 'in2.txt')) as data:
        passwords = list(data.readlines())
        # part1_pieces = solve_part_1(numbers, 2020)
        # print(f"Day 1 part1 answer: {part1_pieces[0]}*{part1_pieces[1]} = {part1_pieces[0]*part1_pieces[1]}")

        # part2_pieces = solve_part_2(numbers, 2020)
        # print(f"Day 1 part2 answer: {part2_pieces[0]}*{part2_pieces[1]}*{part2_pieces[2]} = {part2_pieces[0]*part2_pieces[1]*part2_pieces[2]}")

        print(len(passwords))
