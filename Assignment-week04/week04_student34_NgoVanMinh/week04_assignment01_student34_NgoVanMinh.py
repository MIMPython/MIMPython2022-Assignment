if __name__ == '__main__':
    A = [[1, 2], [3, 0, 4], [2], [4, 5]]
    print(sorted(A, key=lambda A: sum(A)))
    #[[2], [1, 2], [3, 0, 4], [4, 5]]
