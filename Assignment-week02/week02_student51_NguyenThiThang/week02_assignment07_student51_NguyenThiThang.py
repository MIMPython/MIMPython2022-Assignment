from itertools import chain
from unittest import result


def maHoa(str,x):
    str=str.upper()
    result=""
    index=0
    for i in range(len(str)):
        index=ord(str[i])+x
        if (index<ord("Z")):
            result=result+chr(index)
        else:
            result=result+chr(index-1-ord("Z")+ord("A"))
    return result

def giaiMa(str,x):
    str=str.upper()
    result=""
    index=0
    for i in range(len(str)):
        index=ord(str[i])-x
        if (index>ord("A")):
            result=result+chr(index)
        else:
            result=result+chr(index+1+ord("Z")-ord("A"))
    return result

if __name__== '__main__':
    print("Nhap thong diep goc")
    thongDiepGoc = input()
    print("Thong diep sau khi ma hoa voi ROT-13 la:")
    print(maHoa(thongDiepGoc,13))
    print("Nhap thong diep sau khi ma hoa:")
    thongDiepMaHoa = input()
    print("Thong diep sau khi giai ma voi ROT-13 la:")
    print(giaiMa(thongDiepMaHoa,13))

