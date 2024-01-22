import random


class DSU:
    def __init__(self, size: int):
        self.p = list(range(size))

    def find(self, n: int) -> int:
        if self.p[n] == n:
            return n
        self.p[n] = self.find(self.p[n])
        return self.p[n]

    def unite(self, n: int, m: int, with_order: bool = False):
        n, m = self.find(n), self.find(m)
        if n == m:
            return

        if not with_order and random.randint(0, 1):
            n, m = m, n
        self.p[n] = m
