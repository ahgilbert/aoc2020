from os import path
def fetch_input(fn):
    with open(path.join('.', fn)) as data:
        text = data.read()
        raw = text.split('\n\n')
        return raw

def bounded(target, lo, hi):
    return int(target) >= lo and int(target) <= hi
def validHeight(hgt):
    if(bounded[-2:] == "cm"):
        return bounded(hgt[0:-2], 150, 193)
    else:
        return bounded(hgt[0:-2], 59, 76)

def someHexSextuplet(hex):
    return hex[0] == '#'
def eyeColor(ecl):
    allowable = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    return set([ecl]).issubset(allowable)
def nineDigitNum(ndn):
    return len(ndn) == 9 and \
        int(ndn)

def full_validation(passport):
    validations = {
        'byr': lambda test: len(test) == 4 and 1920 <= int(test) <= 2002,
        'iyr': lambda test: len(test) == 4 and 2010 <= int(test) <= 2020,
        'eyr': lambda test: len(test) == 4 and 2020 <= int(test) <= 2030,
        'hgt': lambda test: valid_height(test),
        'hcl': lambda test: re.match(r'^#[0-9a-f]{6}$', test),
        'ecl': lambda test: test in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda test: re.match(r'^[0-9]{9}$', test),
        'cid': lambda test: True,
    }


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

    print("part 2: ", len(passports))