print("Bài 9: Tic-tac-toe trên bàn cờ cỡ 3x3")

print()
#TRÌNH BÀY LUẬT CHƠI TIC-TAC-TOE TỰ THIẾT KẾ
"""
Trò chơi 2 người chơi với Player1 (X) tương ứng với 1 và Player2 (O) tương ứng với 2
Chọn người đi trước là X hoặc O đều được
Người thắng khi và chỉ khi 1 trong các hàng hoặc các cột hoặc đường chéo chính/phụ cùng X hoặc O
Cả hai đều hòa ván khi và chỉ khi không có ai thắng 
Nếu tích nhầm vào ô đã tích thì sẽ xem ai có nhiều X hoặc O hơn sẽ giành chiến thắng
"""

#Vẽ hình sau khi chạy 
def drawBoard(A):
    print(A[0] + ' | ' + A[1] + ' | ' + A[2])
    print('- + - + -')
    print(A[3] + ' | ' + A[4] + ' | ' + A[5])
    print('- + - + -')
    print(A[6] + ' | ' + A[7] + ' | ' + A[8])

nguoi = int(input("Chọn người muốn đi trước: "))

if nguoi == 1:
    print("Người X sẽ đi trước")
    print()
    d = 0
    A = ["_"]*9
    for i in range(9):

        #Thứ tự đặt lần lượt của X và O
        if d == 0:
            vitri = int(input("Nhập ô player1 muốn đặt: "))
        else:
            vitri = int(input("Nhập ô player2 muốn đặt: "))

        #Đặt vị trí X và O
        if A[vitri-1] == "_":
            if d % 2 == 0:
                A[vitri-1] = "X"
                d += 1
            else:
                A[vitri-1] = "O"
                d -= 1

            #Kiểm tra người thắng qua 8 trường hợp

            #Hàng 1
            if A[0] == A[1] == A[2] != "_":
                if A[0] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[0] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass

            #Hàng 2
            elif A[3] == A[4] == A[5] != "_":
                if A[3] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[3] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Hàng 3
            elif A[6] == A[7] == A[8] != "_":
                if A[6] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[6] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Cột 1
            elif A[0] == A[3] == A[6] != "_":
                if A[0] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[0] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Cột 2
            elif A[1] == A[4] == A[7] != "_":
                if A[1] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[1] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Cột 3
            elif A[2] == A[5] == A[8] != "_":
                if A[2] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[2] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Đường chéo chính
            elif A[0] == A[4] == A[8] != "_":
                if A[0] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[0] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Đường chéo phụ
            elif A[2] == A[4] == A[6] != "_":
                if A[2] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[2] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            else:
                pass 

        else:
            print("Người dùng nhập sai")
            if A.count("X") > A.count("O"):
                print("Player1 thắng")
            elif A.count("X") < A.count("O"):
                print("Player2 thắng")
            else:
                print("Player1 và Player2 hòa ván do sự cố")
            break
        print(A)
        drawBoard(A)
        print()

    else:
        print("Player1 và Player2 đều hòa ván")
        drawBoard(A)
        print(A)

elif nguoi == 2:
    print("Người O sẽ đi trước")
    print()
    d = 0
    A = ["_"]*9
    for i in range(9):

        #Thứ tự đặt lần lượt của O và X
        if d == 0:
            vitri = int(input("Nhập ô player2 muốn đặt: "))
        else:
            vitri = int(input("Nhập ô player1 muốn đặt: "))

        #Đặt vị trí O và X
        if A[vitri-1] == "_":
            if d % 2 == 0:
                A[vitri-1] = "O"
                d += 1
            else:
                A[vitri-1] = "X"
                d -= 1

            #Kiểm tra người thắng qua 8 trường hợp

            #Hàng 1
            if A[0] == A[1] == A[2] != "_":
                if A[0] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[0] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass

            #Hàng 2
            elif A[3] == A[4] == A[5] != "_":
                if A[3] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[3] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Hàng 3
            elif A[6] == A[7] == A[8] != "_":
                if A[6] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[6] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Cột 1
            elif A[0] == A[3] == A[6] != "_":
                if A[0] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[0] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Cột 2
            elif A[1] == A[4] == A[7] != "_":
                if A[1] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[1] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Cột 3
            elif A[2] == A[5] == A[8] != "_":
                if A[2] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[2] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Đường chéo chính
            elif A[0] == A[4] == A[8] != "_":
                if A[0] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[0] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            
            #Đường chéo phụ
            elif A[2] == A[4] == A[6] != "_":
                if A[2] == "X":
                    print("Player1 thắng")
                    print(A)
                    drawBoard(A)
                    break
                elif A[2] == "O":
                    print("Player2 thắng")
                    print(A)
                    drawBoard(A)
                    break
                else:
                    pass
            else:
                pass 
            
        else:
            print("Người dùng nhập sai")
            if A.count("X") > A.count("O"):
                print("Player1 thắng")
            elif A.count("X") < A.count("O"):
                print("Player2 thắng")
            else:
                print("Player1 và Player2 hòa vốn do sự cố")
            break
        print(A)
        drawBoard(A)
        print()
    else:
        print("Player2 và Player1 đều hòa ván")
        print(A)
        drawBoard(A)
else:
    print("Không có người chơi này")
