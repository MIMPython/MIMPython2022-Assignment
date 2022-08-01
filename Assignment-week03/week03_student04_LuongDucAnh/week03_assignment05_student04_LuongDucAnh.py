from getpass import getpass #ẩn nội dung nhập vào, nhằm đảm bảo tính công bằng

moves = {"kéo": 0, "búa": 1, "bao": 2}

def playerInput(): #Hàm nhận lựa chọn của người chơi
    player = int(getpass("Hãy nhập lựa chọn: "))
    while player not in moves.values():
        player = getpass("Lựa chọn không hợp lệ, hãy nhập lại: ")
    return player

def findWinner(player1, player2): #Hàm xác định người thắng
    diff = player1 - player2
    if (abs(diff) == 1 and diff > 0) or (abs(diff) == 2 and diff < 0):
        return True #Người chơi thứ nhất thắng
    else:
        return False #Người chơi thứ 2 thắng

def main():
    print ("Trò chơi kéo - búa - bao")
    while True:
        print (f"\n{moves}")
        print ("Người chơi thứ nhất: ")
        player1 = playerInput()
        print ("Người chơi thứ hai: ")
        player2 = playerInput()
        if player1 == player2:
            print ("Hoà")
        else:
            if findWinner(player1, player2):
                print ("Người chơi thứ nhất thắng")
            else:
                print ("Người chơi thứ hai thắng")
        if input("Bạn có muốn chơi lại (y/n): ") == "y":
            continue
        else:
            break

if __name__ == "__main__":
    main()