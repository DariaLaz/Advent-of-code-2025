
from math import sqrt


class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}
        self.count = len(items)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def unite(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False

        self.parent[p2] = p1
        self.count -= 1
        return True


def dist(x1, x2):
    return sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2 + (x1[2]-x2[2])**2)
