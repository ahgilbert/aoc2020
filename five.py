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
    col = ''.join(list(map(normalizeCharLR, boarder[7:11])))
    return int(row, 2), int(col, 2)

def seat_id(code):
    seat = to_seat(code)
    row = seat[0]
    col = seat[1]
    return (8 * row) + col

def test():
    return to_seat("BFBBBBBLLR")


if __name__ == '__main__':
    manifest = fetch_input()
    seatIds = list(map(seat_id, manifest))

    maxSeatId = -1
    maxSeat = ""

    for passenger in manifest:
        seatId = seat_id(passenger.strip())
        if seatId > maxSeatId:
            maxSeatId = seatId
            maxSeat = passenger

    print(f"{maxSeat.strip()} at {maxSeatId}")
    # Hey reader, I solved part 2 with a bunch of bash hackery:
    #     #> sed 's/[RL]//g' | sort | uniq -c | grep 7
    # showed me the row, and
    #     #> grep 'BFBFBFF' in5.txt | sort
    # gave me a sorted list to eyeball
