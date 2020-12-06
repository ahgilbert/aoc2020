from os import path

def fetch_input():
    with open(path.join('.', 'in5.txt')) as data:
        return list(data.readlines())

def to_seat(boarder):
    def normalizeCharBF(c):
        return "1" if c == "B" else "0"
    def normalizeCharLR(c):
        return "1" if c == "R" else "0"
    row = ''.join(list(map(normalizeCharBF, boarder[0:7])))
    col = ''.join(list(map(normalizeCharLR, boarder[7:])))
    return int(row, 2), int(col, 2)

def seat_id(seat):
    row = seat[0]
    col = seat[1]
    return (8 * row) + col

def test():
    return to_seat("BFBBBBBLLR")


if __name__ == '__main__':
    manifest = fetch_input()
    seats = map(seat_id, map(to_seat, manifest))
    foo = -1
    for seat in seats:
        if seat > foo:
            foo = seat
    print(foo) # 1004 is too high