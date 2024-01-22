from typing import Tuple, Set, List

from lab1.dsu import DSU


class MazeSolver:
    def __init__(self, partitions: Set[Tuple[int, int]], maze_height: int, maze_width: int):
        self._maze_h = maze_height
        self._maze_w = maze_width
        self._dsu = DSU(maze_height * maze_width)

        maze: List[bool] = [True for _ in range(maze_height * maze_width)]
        for coord in partitions:
            x, y = coord
            maze[self._index_by_coord(x, y)] = False
        self._maze = maze

    def _index_by_coord(self, x: int, y: int) -> int:
        return x + y * self._maze_w

    def _has_exit(self, idx: int) -> bool:
        final = self._dsu.find(idx)
        return (self._maze[final]
                and (final % self._maze_w in {0, self._maze_w - 1}
                or final // self._maze_w in {0, self._maze_h - 1}))

    def _unite(self, idx1: int, idx2: int):
        if self._has_exit(idx1) and not self._has_exit(idx2):
            self._dsu.unite(idx2, idx1, True)
        elif self._has_exit(idx2) and not self._has_exit(idx1):
            self._dsu.unite(idx1, idx2, True)
        else:
            self._dsu.unite(idx1, idx2)

    def preprocess(self):
        for y in range(self._maze_h):
            for x in range(self._maze_w):
                idx = self._index_by_coord(x, y)
                if not self._maze[idx]:
                    continue

                if self._maze[idx - 1]:
                    self._unite(idx, idx - 1)
                if self._maze[idx - self._maze_w]:
                    self._unite(idx, idx - self._maze_w)

    def query(self, x: int, y: int) -> bool:
        return self._has_exit(self._index_by_coord(x, y))
