def name_scores():
    # Mở file
    file = open('names.txt')
    # Đọc file
    str_file = file.read()
    # Chia nhỏ
    names = str_file.split(',')
    # xóa "
    names = [name.strip('"') for name in names]
    # sắp xếp
    names.sort()

    total_name_scores = 0
    for i in range(len(names)):
        for j in range(len(names[i])):
            total_name_scores += ord(names[i][j]) - ord('A') + 1
        total_name_scores += (i + 1)
    return total_name_scores


if __name__ == '__main__':
    print(name_scores())
