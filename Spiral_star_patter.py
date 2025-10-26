n = 7
matrix = [[' ' for _ in range(n)] for _ in range(n)]
left, right, top, bottom = 0, n - 1, 0, n - 1
char = '*'

while left <= right and top <= bottom:
    for i in range(left, right + 1):
        matrix[top][i] = char
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = char
    right -= 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = char
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = char
    left += 1

for row in matrix:
    print(''.join(row))
