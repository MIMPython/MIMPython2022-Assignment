"""
    Luật chơi: Tic Tac Toe là một trò chơi trên giấy và bút dành cho hai 
người chơi. Mỗi người sẽ chọn một ký hiệu X và O và thay nhau ghi vào 
các khoảng trống trong 9 ô vuông lưới 3x3. Người chơi nào tạo được 
một hàng với 3 ký tự liên tiếp trên cùng một hàng ngang, dọc hoặc chéo
là người thắng cuộc.
"""

from pickle import TRUE
from re import T


chessBoard= [[" ", " ", " "], 
             [" ", " ", " "],
             [" ", " ", " "]]


def checkWin():
    if (chessBoard[0][0] == chessBoard[0][1] and chessBoard[0][0] == chessBoard[0][2] and chessBoard[0][0] != " "):
        return True
    elif (chessBoard[1][0] == chessBoard[1][1] and chessBoard[1][0] == chessBoard[1][2] and chessBoard[1][0] != " "):
        return TRUE
    elif (chessBoard[2][0] == chessBoard[2][1] and chessBoard[2][0] == chessBoard[2][2] and chessBoard[2][0] != " "):
        return True
    elif (chessBoard[0][0] == chessBoard[1][0] and chessBoard[0][0] == chessBoard[2][0] and chessBoard[0][0] != " "):
        return True
    elif (chessBoard[0][1] == chessBoard[1][1] and chessBoard[0][1] == chessBoard[2][1] and chessBoard[0][1] != " "):
        return True
    elif (chessBoard[0][2] == chessBoard[1][2] and chessBoard[0][2] == chessBoard[2][2] and chessBoard[0][2] != " "):
        return True
    elif (chessBoard[0][0] == chessBoard[1][1] and chessBoard[0][0] == chessBoard[2][2] and chessBoard[0][0] != " "):
        return True
    elif (chessBoard[0][2] == chessBoard[1][1] and chessBoard[0][2] == chessBoard[2][0] and chessBoard[0][2] != " "):
        return True
    else: return False
def writeChess():
    print(chessBoard[0])
    print(chessBoard[1])
    print(chessBoard[2])
    print()
writeChess()
i=1
while (i <= 9):
    if (i % 2 == 1):
        row = int( input("người chơi thứ nhất chọn hàng: "))
        column = int(input("người chơi thú nhất chọn cột: "))
        chessBoard[row][column] = "x"
        if (checkWin() == True):
            writeChess()
            print("NGƯỜI THỨ NHẤT CHIẾN THẮNG")
            break
        writeChess()
    else: 
        row = int( input("người chơi thứ hai chọn hàng: "))
        column = int( input("người chơi thú hai chọn cột: "))
        chessBoard[row][column] = "o"
        if (checkWin() == True):
            writeChess()
            print("NGƯỜI THỨ HAI CHIẾN THẮNG")
            break
        writeChess()
    i += 1
if (i == 10 and checkWin() == False):
    print("Hòa")