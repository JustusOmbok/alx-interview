#!/usr/bin/python3

import sys


def solve(row, column):
    """
    Solve the N Queens problem using backtracking.

    Args:
        row (int): The current row being considered.
        column (int): The total number of queens to be placed.

    Returns:
        List[List[int]]: List of solutions
        where each solution is represented as a list of queen positions.
    """
    solver = [[]]
    for q in range(row):
        solver = place_queen(q, column, solver)
    return solver


def place_queen(q, column, prev_solver):
    """
    Place a queen in the current row if it is safe to do so.

    Args:
        q (int): The current row.
        column (int): The total number of queens to be placed.
        prev_solver (List[List[int]]): Previous solutions.

    Returns:
        List[List[int]]: Updated solutions
        after placing a queen in the current row.
    """
    solver_queen = []
    for array in prev_solver:
        for x in range(column):
            if is_safe(q, x, array):
                solver_queen.append(array + [x])
    return solver_queen


def is_safe(q, x, array):
    """
    Check if it's safe to place a queen at a given position.

    Args:
        q (int): Current row.
        x (int): Column position to check.
        array (List[int]): Current solution configuration.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """
    Initialize the N Queens problem by validating command-line arguments.

    Returns:
        int: The number of queens specified by the user.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        the_queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if the_queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return the_queen


def n_queens():
    """
    Main function to solve and print N Queens solutions.
    """
    the_queen = init()
    solver = solve(the_queen, the_queen)
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
