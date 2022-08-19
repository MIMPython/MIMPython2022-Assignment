from os import lstat
import numpy as np
# chương trình chạy vòng lặp vô tận sử dụng while là:
# while 1:
#     print('Python')

# chương trình chạy vòng lặp vô tận sử dụng for:
# list = ['An']
# for i in list:
#     print(i)
#     list.append('An')

# chương trình chạy vô hạn sử dụng vòng lặp for mà đối tượng được duyệt (sau từ khóa in) không phải là một list, tuple, set, hay dictionary:
from itertools import cycle
for x in cycle(range(5)):
    print('Python')
