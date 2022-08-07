def sortList(A):
    return sorted(A, key = lambda x: sum(x))

if __name__ == "__main__":
    A = [[1, 3, 4], [3, 5], [5, 1], [2, -5], [-3, 0.8]]

    print(sortList(A))  # [[2, -5], [-3, 0.8], [5, 1], [1, 3, 4], [3, 5]]
