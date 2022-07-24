import string
from tokenize import String


name = input('input name:')
stt_tuanhoc = int( input (' input stt tuan học :'))
stt_baitap = int(input ('input stt bài tập: '))
def infor ():
    print('week',stt_tuanhoc,'_assignment',stt_baitap,'_studentZZ_',name,'.py')
infor()