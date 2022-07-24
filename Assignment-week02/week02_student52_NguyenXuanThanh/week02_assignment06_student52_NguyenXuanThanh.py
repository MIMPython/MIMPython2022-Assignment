# Bài tập 6. Viết một hàm tìm tất cả các nghiệm thực (phân biệt) của phương trình

# ax2+bx+c=0.
# Input: ba số a, b, c bất kỳ
# Output: một tuple chứa tất cả các nghiệm thực (phân biệt), xếp theo thứ tự tăng dần, của phương trình ax2+bx+c=0.

import math

def giaiPTBac2(a, b, c):
    if (a == 0):
        if (b == 0):
            print ();
        else:
            print (-c / b);
        return;
    delta = b * b - 4 * a * c;
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        print (x1,x2);
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print(x1);
    else:
        print();
giaiPTBac2(1, 1, -2) # (1,-)
giaiPTBac2(1, 2, 1) # (-1, )
giaiPTBac2(1, 4, 5) # ()     
