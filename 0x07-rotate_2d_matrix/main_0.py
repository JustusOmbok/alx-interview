#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    matrix2 = [[2, 5, 6, 4],
               [3, 4, 6, 7],
               [6, 9, 7, 8],
               [4, 5, 6, 8]]

    rotate_2d_matrix(matrix1)
    print(matrix1)
    rotate_2d_matrix(matrix2)
    print(matrix2)
