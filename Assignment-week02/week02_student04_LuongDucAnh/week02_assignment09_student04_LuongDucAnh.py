import time
count = 0

board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def showBoard(): #Hiển thị bảng cờ caro
    for i in range (3):
        for j in range (3):
            print (f"{board[i][j]} ", end = "")
        print ("")
        
def fixSpot(row, col, player): #Cập nhật lại bảng
    board[row - 1][col - 1] = player
    global count
    count += 1

def checkBoard():
    for i in range (3): #Kiểm tra hàng
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != "-":
            if board[i][0] == "X":
                return 1
            else:
                return 2
    for i in range (3): #Kiểm tra cột
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != "-":
            if board[0][i] == "X":
                return 1
            else:
                return 2
    if board[0][0] == board[1][1] and board[2][2] == board[0][0] and board[0][0] != "-": #Kiểm tra đường chéo
            if board[0][0] == "X":
                return 1
            else:
                return 2
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != "-": #Kiểm tra đường chéo
            if board[0][2] == "X":
                return 1
            else:
                return 2

def isPlayerWin():
    if checkBoard() == 1:
        print ("Người chơi 1 thắng")
        showBoard()
        return True
    elif checkBoard() == 2:
        print ("Người chơi 2 thắng")
        showBoard()
        return False
    else:
        isDraw()

def isDraw():
    global count
    if count == 9:
        print ("Hai người hoà")

def demo():
    print ("Lượt người chơi 1: ")
    fixSpot(1, 1, "X")
    time.sleep(3)
    showBoard()
    isPlayerWin()
    
    print ("Lượt người chơi 2: ")
    fixSpot(1, 2, "O")
    time.sleep(3)
    showBoard()
    isPlayerWin()
    
    print ("Lượt người chơi 1: ")
    fixSpot(2, 2, "X")
    time.sleep(3)
    showBoard()
    isPlayerWin()
    
    print ("Lượt người chơi 2: ")
    fixSpot(3, 3, "O")
    time.sleep(3)
    showBoard()
    isPlayerWin()
    
    print ("Lượt người chơi 1: ")
    fixSpot(3, 1, "X")
    time.sleep(3)
    showBoard()
    isPlayerWin()
    
    print ("Lượt người chơi 2: ")
    fixSpot(2, 1, "O")
    time.sleep(3)
    showBoard()
    isPlayerWin()
    
    print ("Lượt người chơi 1: ")
    fixSpot(1, 3, "X")
    time.sleep(3)
    showBoard()
    isPlayerWin()

def main():
    print ("Tic-tac-toe")
    print (f"Hai người chơi, người dùng ký hiệu O, người kia dùng ký hiệu X, lần lượt điền ký hiệu của mình vào các ô. Người thắng là người có thể tạo được đầu tiên một dãy ba ký hiệu của mình, ngang dọc hay chéo đều được.")
    demo()
        
main()
print (f"Số bước đi: {count}")