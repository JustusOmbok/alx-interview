#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal Triangle upto the nth row.
    Args:
    n: Int, number of rows for pascal's triangle
    Returns: List of lists rpresenting pascal's tringle
    """
    
    triangle = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
