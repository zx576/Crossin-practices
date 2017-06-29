# https://paste.ubuntu.com/24945533/
# 林昱辰
# 运行有问题
def helix_matrix_generator(helix_matrix, width, current_width, direction, count, position):
    if(current_width > 0):
        for a in range(0, current_width):
            if(direction):
                position += 1
            else:
                position -= 1
            helix_matrix[position - 1] = count
            count += 1
        for a in range(0, current_width-1):
            if(direction):
                position += width
            else:
                position -= width
            helix_matrix[position - 1] = count
            count += 1
        if(direction):
            return helix_matrix_generator(helix_matrix, width, current_width - 1, False, count, position)
        else:
            return helix_matrix_generator(helix_matrix, width, current_width - 1, True, count, position)
    else:
        return helix_matrix

def main():
    width = input('Input the width of helix_matrix>> ')
    if not width.strip():
        width = 4
    width = int(width)
    size = width * width
    helix_matrix = list(range(size))

    helix_matrix = helix_matrix_generator(helix_matrix, width, width, True, 1, 0)

    temp = 0
    for x in range(width):
        for y in range(width):
            print(helix_matrix[temp + y], end=' ')
        print('\n')
        temp += width


if __name__ == "__main__":
    main()
