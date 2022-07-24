def one_digit(number):
    if number/10 < 1:
        return '0' + str(number)
    else:
        return str(number)


def file_name(name, week, assignment):

    print('week' + one_digit(week) + '_assignment' + one_digit(assignment) +
          '_studentZZ_' + name + '.py')


if __name__ == '__main__':
    file_name('NguyenNgocAnh', 2, 3)
