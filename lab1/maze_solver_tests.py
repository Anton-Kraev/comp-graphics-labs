from lab1.maze_solver import MazeSolver


def simple_maze_test():
    """
    # # . # #
    . . . . #
    . # # # #
    # . # . #
    # . # # #
    """

    maze = {
        (0, 0), (0, 3), (0, 4),
        (1, 0), (1, 2),
        (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 2), (3, 4),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
    }
    solver = MazeSolver(maze, 5, 5)
    solver.preprocess()

    results = {
        (0, 0, False), (0, 1, True), (0, 2, True), (0, 3, False), (0, 4, False),
        (1, 0, False), (1, 1, True), (1, 2, False), (1, 3, True), (1, 4, True),
        (2, 0, True), (2, 1, True), (2, 2, False), (2, 3, False), (2, 4, False),
        (3, 0, False), (3, 1, True), (3, 2, False), (3, 3, False), (3, 4, False),
        (4, 0, False), (4, 1, False), (4, 2, False), (4, 3, False), (4, 4, False)
    }

    for x, y, expected in results:
        assert solver.query(x, y) == expected


def large_maze_test():
    size = 1_000_000
    maze = {
        (x, y)
        for x in range(0, size)
        for y in range(0, size)
        if x in {0, 2} or y in {0, 2}
    }
    solver = MazeSolver(maze, size, size)
    solver.preprocess()

    assert solver.query(1, 3) and solver.query(3, 1)
    assert not (solver.query(1, 1) or solver.query(2, 2))
