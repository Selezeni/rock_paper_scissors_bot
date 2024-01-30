def rot90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix2 = rot90(matrix)

print(matrix2)
print()
print(matrix)
