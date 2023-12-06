#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    if matrix:
        for i in matrix:
            neoRow = []
            for j in i:
                neoRow.append(j ** 2)
            squares.append(neoRow)
    return (squares)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)