from common import run_input
from day_08_common import UnionFind, dist


def solution(coordinates):
    uf = UnionFind(coordinates)

    pairs = []
    n = len(coordinates)

    for i in range(n):
        for j in range(i + 1, n):
            a, b = coordinates[i], coordinates[j]
            pairs.append((dist(a, b), a, b))

    pairs.sort(key=lambda x: x[0])

    for _, a, b in pairs:
        if uf.unite(a, b) and uf.count == 1:
            return a[0] * b[0]


run_input(day=8, task=2, solution=solution,
          process_line=lambda x: tuple(map(int, x.split(","))))
