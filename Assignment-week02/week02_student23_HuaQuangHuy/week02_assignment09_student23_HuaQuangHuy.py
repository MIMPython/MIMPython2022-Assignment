# Bài tập 9: Tic tac toe:
"""
Luật chơi: 
- 2 người chơi điền ký tự x, o vào bàn cờ 3 * 3 ô vuông,
- Khi một ô được điền thì 2 người chơi không được thay đổi giá trị của ô đó
- Khi trong bàn cờ tạo thành một hàng ngang hoặc một hàng dọc, hoặc một đường chéo 3 ô liên tiếp các ký tự giống nhau thì người điền ký tự đó thắng.
- Nếu cả 9 ô trên bàn cờ đều được điền mà chưa tạo thành bất kỳ một hàng dọc, hoặc ngang, hoặc chéo 3 ô có ký tự giống nhau thì 2 người chơi hòa.

Input: Ma trận 3 * 3 chỉ có giá trị các của các ô là 1, 0, 10;
khi người chơi 1 chọn một ô thì ô đó có giá trị 1. Người thứ 2 chọn thì ô đó có giá trị -1, Nếu không điền thì ô có giá trị 0;

Output: kết luận 1 trong 2 người thắng hoặc 2 người hòa nhau

"""


def checkResultTOT(result):
    # kiem tra hang
    for row in result:
        sumRow = 0
        for cell in row:
            sumRow += cell
        if sumRow == 3:
            return 1
        elif sumRow == -3:
            return -1
        else:
            continue

    # kiem tra cot:
    for i in range(len(result)):
        sumColumn = 0
        for j in range(len(result[i])):
            sumColumn += result[j][i]
        if sumColumn == 3:
            return 1
        elif sumColumn == -3:
            return -1
        else:
            continue

    # Kiem tra duong cheo


if __name__ == '__main__':
    result = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    checkResultTOT(result)
