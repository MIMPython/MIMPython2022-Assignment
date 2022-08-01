# Bài tập 5. (rock-paper-scissors game)
# (a) Viết một chương trình để hai người có thể
# chơi trò chơi kéo - búa - bao với nhau.

# (b) Cách tiếp cận đơn giản là cho phép hai người
# chơi A, B lần lượt đưa ra lựa chọn và nhập nó vào
# chương trình thông qua bàn phím (giả sử A nhập trước).
# Cách chơi như vậy không công bằng vì ở mỗi lượt chơi B
# luôn biết được lựa chọn của A trước khi B đưa ra lựa chọn.
# Thiết kế chương trình để đảm bảo tính công bằng cho trò chơi.

# (c) Có thể hiểu tính công bằng theo nghĩa nào khác?

import getpass


def rock_paper_scissors():
    dictionary = {0: 'kéo', 1: 'búa', 2: 'bao'}
    game_matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    while True:
        print('Nhập lựa chọn: \n 0 - kéo \n 1 - búa \n 2 - bao \n')

        choice_A = int(getpass.getpass('Người A: '))
        while choice_A > 2 or choice_A < 0:
            choice_A = int(getpass.getpass('Nhập lại (0 <= lựa chon <= 2): '))
        choice_B = int(getpass.getpass('Người B: '))
        while choice_B > 2 or choice_B < 0:
            choice_B = int(getpass.getpass('Nhập lại (0 <= lựa chon <= 2): '))

        if game_matrix[choice_A][choice_B] == 1:
            print('A win! A: {} --> B: {}'.format(dictionary[choice_A], dictionary[choice_B]))
        else:
            if game_matrix[choice_A][choice_B] == 0:
                print('Draw! A: {} -- B: {}'.format(dictionary[choice_A], dictionary[choice_B]))
            else:
                print('B win! A: {} <-- B: {}'.format(dictionary[choice_A], dictionary[choice_B]))
        continue_game = input('Tiếp tục? \n Y/y - Có \n N/n - Không \n')
        if continue_game == 'N' or continue_game == 'n':
            break


if __name__ == '__main__':
    rock_paper_scissors()

# (c) Công bằng khi cả hai đều không đoán trước được mình sẽ thắng hay không
# có thể cho A và B cùng nhập một số (hoặc kí tự, sau đó chuyển về thứ tự của
# kí tự trong bảng mã), lấy ngẫu nhiên một số trong khoảng chọn của A và B
# lấy số đó % 3 -> [0, 1, 2] định nghĩa chiến thắng bởi các số.
