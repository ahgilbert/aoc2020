from os import path

def fetch_input(fn):
    with open(path.join('.', fn)) as data:
        text = data.read()
        raw = text.split('\n\n')
        return raw

requiredFields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])

if __name__ == '__main__':
    sloppy = fetch_input('in4.txt')
    passports = []
    for slop in sloppy:
        d = {}
        items = slop.split()
        kvps = [foo.split(':') for foo in items]
        for kvp in kvps:
            d[kvp[0]] = kvp[1]
        passports.append(d)

    part1 = 0
    for passport in passports:
        ks = set(passport.keys())
        if len(ks.intersection(requiredFields)) == 7:
            part1 = part1 + 1

    print("part 1: ", part1)