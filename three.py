from os import path
# read input and initialize array
# check bounds

class Forest:
    height = 0
    width = 0
    contents = [[]]

    def __init__(self, lines):
        self.contents = [[c == '#' for c in row.strip()] for row in lines]
        self.height = len(self.contents)
        self.width = len(self.contents[0])

    def tree_at(self, c, r):
        print(c,r)
        return self.contents[r][c]

    def in_bounds(self, c, r):
        return c >= 0 and r >= 0 and c < self.width and r < self.height

def fetch_input():
    with open(path.join('.', 'in3.txt')) as data:
        rows = list(data.readlines())
        f = Forest(rows)
        return f

def count_collisions(forest, rstep, dstep):
    c = 0
    r = 0
    collisions = 0
    while forest.in_bounds(c,r):
        if(forest.tree_at(c,r)):
            collisions = collisions + 1
        c = (c + rstep) % forest.width
        r = r + dstep
    return collisions

if __name__ == '__main__':
    forest = fetch_input()
    a = count_collisions(forest, 1, 1)
    b = count_collisions(forest, 3, 1)
    c = count_collisions(forest, 5, 1)
    d = count_collisions(forest, 7, 1)
    e = count_collisions(forest, 1, 2)
    print("part 1: ", b)
    print("part 2: ", a * b * c * d * e)
