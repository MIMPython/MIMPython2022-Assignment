print("Bài 7: Bad Luck Probability")

"""
Tú lơ khơ có 52 lá bài tiêu chuẩn 
Tập hợp từ ba lá bài trở lên là 1 phỏm nếu thỏa mãn 1 trong 2 điều kiện sau:
+ DK1: chúng có cùng giá trị (2 cơ, 2 rô, 2 bích)
+ DK2: chúng có cùng chất và các số nguyên liên tiếp (9 cơ, 10 cơ, J cơ, Q cơ)

Hai lá bài là 1 cạ nếu chúng thuộc 1 phỏm (3 cơ, 3 bích) hoặc (9 rô, J rô)
Một tập các lá bài là ù khan nếu hai lá bài bất kỳ không là 1 cạ
"""

# Ù khan là tập mà không có hai lá bài bất kỳ nào giống nhau về giá trị hoặc đồng chất (2 lá bất kỳ không là 1 cạ)

"""
a) Một tập 9 lá bài rút ngẫu nhiên từ bộ bài là ù khan ?
omega : 'Bốc 9 lá bài từ bộ 52 lá' --> |omega| = 52C9 cách
+ A : 'Tập 9 lá bài ngẫu nhiên là ù khan'
Lá bài: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
Quân bài: Bích, Tép, Rô, Cơ

+ Xét các quân bài lân cận xung quanh 1 lá: (xung quanh +2 và -2)
Mỗi lá bài sẽ có 7 quân lân cận
vd: 5 rô sẽ có các quân lân cận là: (5 bích, 5 tép, 5 cơ) và (3 rô, 4 rô, 6 rô, 7 rô)
Riêng lá Q và 2 sẽ có 6 lân cận 
vd: Q bích sẽ có các lân cận là: (Q tép, Q rô, Q cơ) và (10 bích, J bích, K bích)
Riêng lá K và A sẽ có 5 lân cận
vd: K cơ sẽ có các lân cận là: (K bích, K tép, K rô) và (J cơ, Q cơ)

--> Để là ù khan thì bỏ hết các quân lân cận xung quanh lá bài đấy 
(chọn ra các lá để nó là ù khan)

--> Một tập ù khan luôn gồm 13 lá bài
Ta sẽ chọn ra 1 tập con bất kỳ từ những tập bài là ù khan
=> P(A) = 13C9 / 52C9

b) Một tập 10 lá bài rút ngẫu nhiên từ bộ bài là ù khan ?
=> P(B) = 13C10 / 52C10
"""
