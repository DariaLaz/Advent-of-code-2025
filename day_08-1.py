from common import run_input
from day_08_common import UnionFind, dist


def largest(uf: UnionFind):
    sizes = {}
    for node in uf.parent:
        root = uf.find(node)
        sizes[root] = sizes.get(root, 0) + 1

    sed = sorted(sizes.values(), reverse=True)[:3]
    result = 1

    for s in sed:
        result *= s

    return result


def solution(coordinates):
    uf = UnionFind(coordinates)

    pairs = []
    n = len(coordinates)

    for i in range(n):
        for j in range(i+1, n):
            a, b = coordinates[i], coordinates[j]
            pairs.append((dist(a, b), a, b))

    pairs.sort(key=lambda x: x[0])

    for _, a, b in pairs[:1000]:
        uf.unite(a, b)

    return largest(uf)


run_input(day=8, task=1, solution=solution,
          process_line=lambda x: tuple(map(int, x.split(","))))
