from os import name
def file (name, week, assignment):
    filename = 'week' + week + '_' + 'assignment' +  % assignment + '_' + name + '.py'
    return filename

if __name__ == '__main__':
    print(file ('TaKhanhLy', 2, 3))
    