import time
from turtle import right

"""
Chương trình hiện đang gặp lỗi!
Cụ thể: theo trò chơi thì kiến sẽ tiến trước rồi sau đấy mới quay đầu
tuy nhiên chương trình đang thực hiện ngược lại là quay trước rồi mới
đi dẫn tới két lại ở một ô 4,
Ngoài ra khi có cải thiện 1 chút thì mặc dù có phương thức để cấp phát
thêm và mở rộng vị trí bàn chơi ra vô hạn tuy nhiên vẫn có 1 vài trường
hợp vẫn cấp phát nhưng lại di chuyển sang cạnh bên kia trước rồi mới
Cấp phát tiếp kích thước của mảng và điều này cũng đôi khi dẫn tới một
vài trường hợp bị lỗi index out of bound. Rất mong mọi người đọc và cho
mình xin 1 vài giải pháp khắc phục lỗi này
"""

# Nước đi tiếp theo
def nextMove(board: list, row: int, col: int):
    if board[row][col]:
        board[row][col] = 0
        return "l"

    board[row][col] = 1
    return "r"

# Di chuyển
def move(board: list, status: str, row: int, col: int):
    clockwise = {"l": (1,0),"u": (0,-1),"r": (-1, 0),"d": (0, 1)}
    rigthKey = list(clockwise.keys())
    right = "".join(rigthKey)
    counterClockwise = {"u":(0, -1),"r": (-1, 0),"d":(0, 1),"l":(1,0)}
    leftKey = list(counterClockwise.keys())
    left = "".join(leftKey)

    next = nextMove(board, row, col)
    if next == "l":
        return counterClockwise[status], left[left.find(status) - 1]
    return clockwise[status], right[right.find(status) - 1]

# Cấp phát thêm khi kiến chạm cạnh -> Không gian hô hạn      
def outOfBound(board: list[list], row: int, col: int):
    rowSize = len(board)
    colSize = len(board[0])
    while row >= rowSize or row < 0:
        if row >= rowSize:
            board.append([0 for _ in range(colSize)])
            row -= 1
        elif row < 0:
            board.insert(0,[0 for _ in range(colSize)])
            row += 1

    rowSize = len(board)
    colSize = len(board[0])
    while col >= colSize or col < 0:
        if col >= colSize:
            for i in range(rowSize):
                board[i].append(0)
            col -= 1
        elif col < 0:
            for i in range(rowSize):
                board[i].insert(0, 0)
            col += 1
    return board

# In ra bảng trò chơi (Đơn giản)
def printBoard(board: list[list]):
    for i in board:
        print(i)
       
if __name__ == "__main__":
    board = [[0 for _ in range(3)] for _ in range(3)]
    board[1][1] = 1
    row, col = 1, 1
    status = "u"
    turn =  "<"
    round = 1
    i, j = 0, -1
    direction = {"u":"^","r": ">","d":"v","l":"<"}
    while True:
        turn = nextMove(board, row, col)
        row += i
        col += j
        (i, j), status = move(board, status, row, col)
        print(round)
        tmp = board[row],[col]
        board[row][col] = direction[status] 
        printBoard(board)
        round += 1
        board[row][col] = tmp
        time.sleep(1)


"""
Một điều thú vị khi mình chạy chương trình tại trang: http://www.langtonant.com/
Chương trình sẽ chạy xuống góc dưới bên trái theo cùng 1 dạng lặp lại
"""