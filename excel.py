arr = [
    [50, 100, 30, 20, 50],
    [120, 20, 30, 80, 100],
    [70, 40, 50, 40, 150],
    [300, 200, 70, 120, 110],
    [130, 10, 60, 90, 300],
]

buff = [
    [50, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

for i in range(1, len(buff[0])):
    buff[0][i] = buff[0][i - 1] + arr[0][i]

for i in range(1, len(buff)):
    buff[i][0] = buff[i - 1][0] + arr[i][0]

for row in range(1, len(buff)):
    for col in range(1, len(buff[row])):
        buff[row][col] = max(buff[row - 1][col], buff[row][col - 1]) + arr[row][col]