# https://github.com/PeytonXu/learn-python/blob/master/cases/helix_matrix/helix_matrix.py
# 徐大龙
import numpy as np


def generate_helix_matrix(n):
    output_array = np.zeros((n, n), dtype=np.int)
    generate_edges(n, 1, (0, 0), output_array)
    print(output_array)


def generate_edges(n, start_num, start_location, output_array):
    if n < 1:
        return
    if n == 1:
        output_array[start_location[0]][start_location[1]] = start_num
        return

    start = start_num

    # top edge
    i = start_location[0]
    for j in range(start_location[1], start_location[1] + n):
        output_array[i][j] = start
        start += 1

    # right edge
    j = start_location[1] + n - 1
    for i in range(start_location[0] + 1, start_location[0] + n):
        output_array[i][j] = start
        start += 1

    # bottom edge
    i = start_location[0] + n - 1
    for j in range(start_location[1] + n - 2, start_location[1] - 1, -1):
        output_array[i][j] = start
        start += 1

    # left edge
    j = start_location[1]
    for i in range(start_location[0] + n - 2, start_location[0], -1):
        output_array[i][j] = start
        start += 1

    return generate_edges(n - 2, start, (start_location[0] + 1, start_location[1] + 1), output_array)


if __name__ == '__main__':
    generate_helix_matrix(3)
