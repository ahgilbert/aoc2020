from os import path

def fetch_input():
    with open(path.join('.', 'in6.txt')) as data:
        text = data.read()
        groups = text.split('\n\n')
        return [person.split('\n') for person in groups]

def count_qs_union(group):
    uniques = set([])
    for foo in [set(person) for person in group]:
        uniques = uniques.union(foo)
    return len(uniques)

def count_qs_intersect(group):
    ppl = [set(person) for person in group]
    return len(set.intersection(*ppl))

if __name__ == '__main__':
    groups = fetch_input()
    unionCounts = [count_qs_union(group) for group in groups]
    print("part 1: ", sum(unionCounts))

    intersectionCounts = [count_qs_intersect(group) for group in groups]
    print("part 2: ", sum(intersectionCounts))