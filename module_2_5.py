def get_matrix(rows, cols, value):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(value)
        matrix.append(row)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
