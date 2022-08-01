"""
a) So sánh vòng lặp do-while với while
- Vòng lặp while xét điều kiện đúng rồi mới tiếp tục vòng lặp còn sai sẽ thoát.
- do-while khá giống while, tuy nhiên, nó sẽ chạy ít nhất 1 lần cho dùng điều kiện đúng hay không, sau đó kiểm tra điều kiện lặp
nếu đúng sẽ quay lại bước đầu.

"""

# b) Ta hoàn toàn có thể biến đổi while trong python giống với do-while trong C

# VD: 
counter = 0
while True:
    number = int(input("Enter a number between 0 and 10: "))
    counter = counter + 1
    if number < 10 and number > 0:
        break
    if (number > 10 or number < 0) and counter > 7: 
        break