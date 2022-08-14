"""
để một số vừa là số chính phương vừa là số xuôi ngược thì số chính phương đó phải là tích của
hai số xuôi ngược. số xuôi ngược đồng thời là số chính phương bé nhất ta tìm được là 0
tiếp sau đó là 121 = 11 * 11
    hay           11
                * 11
                _____
                  11
                +110
                _____
                 121
trong đó 2 là chữ số trung tâm. chữ số trung tâm này khi cộng không được vượt quá 9 nếu không
sẽ phá vỡ tính đối xứng chẳng hạn
    111111111^2 = 12345678 9 87654321 đối xứng vì chữ số trung tâm không vượt quá 9
    1111111111^2 = 123456790 0 987654321 không đối xứng vì chữ số trung tâm là 10
Vậy chỉ cần chữ số trung tâm luôn giữ được ở khoảng <= 9
thì ta có thể tạo ra một số vừa đảo ngược vừa chính phương
Để chữ số trung tâm không vượt quá 9 thì chữ số trung tâm đó phải là tổng của
nhiều nhất có thể các số 0 chẳng hạn:
    1000000000000000000001 ^ 2 = 1000000000000000000002000000000000000000001
có vô số những số có dạng 1(0)1 như vậy,
điều đó có nghĩ là có vô số số chính phương đồng thời là số đảo ngược
"""


