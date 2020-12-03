from os import path

def parseLine(line):
    bits = line.split(' ')
    bounds = bits[0].split('-')
    target = bits[1][0]
    password = bits[2]

    return (int(bounds[0]), int(bounds[1]), target, password)

def valid(at_least, at_most, target, password):
    count = password.count(target)
    return count >= at_least and count <= at_most

def valid2(idx_a, idx_b, target, password):
    match_a = password[idx_a - 1] == target
    match_b = password[idx_b - 1] == target
    return match_a != match_b

def fetch_input():
    with open(path.join('.', 'in2.txt')) as data:
        passwords = list(data.readlines())
        return passwords


if __name__ == '__main__':
    passwords = fetch_input()
    parsed = [parseLine(a) for a in passwords]
    part1 = [a for a in parsed if valid(*a)]
    part2 = [a for a in parsed if valid2(*a)]
    print(len(part1))
    print(len(part2))
