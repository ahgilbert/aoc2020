from os import path

def fetch_input(fn):
    with open(path.join('.', fn)) as data:
        text = data.read()
        raw = text.split('\n\n')
        return raw

def clean_line(line):
    line = line.replace('\n',' ')

def count_qs_union(group):
    uniques = set([])
    for foo in [set(person) for person in group]:
        uniques = uniques.union(foo)
    return len(uniques)

def count_qs_intersect(group):
    ppl = [set(person) for person in group]
    return len(set.intersection(*ppl))

if __name__ == '__main__':
    sloppy = fetch_input('in4.txt')
    for slop in sloppy:
        d = {}
        items = slop.split()
        kvps = [foo.split(':') for foo in items]
        for kvp in kvps:
            d[kvp[0]] = kvp[1]

        print(d)