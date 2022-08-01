from random import randint

print("Select Dam, La, Keo")
p1 = input()
p2 = randint(0,2)

if p2 == 0:
	p2 = "Dam"
if p2 == 1:
	p2 = "Keo"
if p2 == 2:
	p2 = "La"

print("player 1 select " + str(p1))
print("player 2 select " + str(p2))
print("-------")

if p1 == p2:
	print("Draw")
else:
	if p1 == "Dam":
		if p2 == "La":
			print("player 2 win")
		else:
			print("player 1 win")
	if p1 == "La":
		if p2 == "Keo":
			print("player 2 win")
		else:
			print("player 1 win")
	if p1 == "Keo":
		if p2 == "La":
			print("player 1 win")
		else:
			print("player 2 win")

#Giải thích cách chơi
#Người đầu tiên sẽ chọn bằng cách nhập từ bàn phím Dam/La/Keo, do đây là game random nên người chơi thứ hai sẽ được random bất kì thay vì chọn.