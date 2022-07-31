import math


# trung diem
def trung_diem(A, B):
    I = [(A[0] + B[0]) / 2, (A[1] + B[1]) / 2]
    return I


# phuong trinh duong thang y = ax + b
def duong_thang_di_qua_hai_diem(A, B):
    D0 = (A[1] - B[1]) / (A[0] - B[0])
    D1 = (A[1] - A[0] * D0)
    D = [D0, D1]
    return D


# phuong trinh vuong goc
def vuong_goc(D, I):
    Dv0 = -1 / D[0]
    Dv1 = (I[1] - I[0] * Dv0)
    Dv = [Dv0, Dv1]
    return Dv


def length(A, B):
    return math.sqrt(math.pow(A[0] - B[0], 2) + math.pow(A[1] - B[1], 2))


def tim_C1(Dv, I, len):
    C10 = I[0] + len / (1 + math.pow(Dv[0], 2))
    C11 = Dv[0] * C10 + Dv[1]
    C1 = [C10, C11]
    return C1


def tim_C2(Dv, I, len):
    C20 = I[0] - len / (1 + math.pow(Dv[0], 2))
    C21 = Dv[0] * C20 + Dv[1]
    C2 = [C20, C21]
    return C2


if __name__ == '__main__':
    A = [math.sqrt(3), 0]
    B = [-math.sqrt(3), 0]
    I = trung_diem(A, B)
    lenAB = length(A, B)

    if A[0] == B[0] and A[1] == B[1]:
        print('No solution')
    else:
        if A[0] == B[0]:
            C1 = [I[0], (I[1] + lenAB * math.sqrt(3)/2)]
            C2 = [I[0], (I[1] - lenAB * math.sqrt(3)/2)]
        else:
            if A[1] == B[1]:
                C1 = [I[0] + lenAB * math.sqrt(3)/2, I[1]]
                C2 = [I[0] - lenAB * math.sqrt(3) / 2, I[1]]
            else:
                D = duong_thang_di_qua_hai_diem(A, B)
                Dv = vuong_goc(D, I)

                C1 = tim_C1(Dv, I, lenAB)
                C2 = tim_C2(Dv, I, lenAB)

    print('C1')
    print(C1)
    print('C2')
    print(C2)