"""This method is used to find part of star using BFS

@Arguments:
    check (list[bool]): point have reached
    matrix (list[int]): contain 0 and 1 (Black and white in picture)
    row (int)         :row index
    col (int)         :column index

@Returns:
    Index of all element have vaule 1 in matrix near matrix[row][col]

"""
def partOfStar(check: list, matrix: list, row: int, col: int) -> list:
    index = []
    for i in range(-1,2):
        r = row + i
        if r >= 0 and r < len(matrix):
            for j in range(-1,2):
                c = col + j
                if c >= 0 and c < len(matrix[0]):
                    if i != 0 or j!= 0:
                        if matrix[r][c] and check[r][c]:
                            index.append([r, c])
                        check[r][c] = False
    return index

"""This method is used to count number of star in matrix

@Arguments:
    matrix (list[int]): contain 0 and 1 (Black and white in picture)

@Returns:
    Number of star in matrix

"""
def countStar(matrix: list[int]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    count = 0
    check = [[True for _ in range(n)] for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if matrix[row][col] and check[row][col]:
                count += 1
                index = partOfStar(check, matrix , row, col)
                for k in index:
                    r, c = map(int, k)
                    index.extend(partOfStar(check, matrix, r, c))
            check[row][col] = False
    return count