def file (name, week, ex):
    filename = 'week' + "%02d" % week + '_' + 'assignment' + '%02d' % ex + '_' + name + '.py'
    return filename

if __name__ == '__main__':
    print(file ('duongvana', 3, 5))
    print(file ('nguyenthib', 7, 15))
