import getpass

gameLogic = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}


def compare(a: str, b: str):
    if a in gameLogic.keys():
        if a == b:  # hòa
            return 0
        elif gameLogic[a] == b:  # a thắng cuộc
            return 1
        else:
            return -1
    else:
        raise ValueError()


print('rock-paper-scissors game')
A = getpass.getpass('A, please enter your choice in one of (rock, paper, scissors)')
B = getpass.getpass('B, please enter your choice in one of (rock, paper, scissors)')
try:
    result = compare(A, B)
except ValueError:
    print('your choice is not in (rock, paper, scissors)')
else:
    if result == 0:
        print('Both of you make the same choice')
    elif result == 1:
        print('A is the winner')
    else:
        print('B is the winner')

# c. tính công bằng ở đây có thể hiểu là sự bảo mật về giá trị, B không nên biết giá trị A nhập vào cho đến khi
# kết thúc trò chơi
