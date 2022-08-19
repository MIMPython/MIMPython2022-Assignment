# Bai 9

"""
Để dễ dàng xử lý bài toán mình sẽ đưa nó về dạng đơn giản và dễ hình dung hơn.
Quy bài toán cần giải quyết về bài toán tìm quỹ tích 3 điểm A, B, C trên 1 đường tròn
bán kính R = 2 sao cho AB + BC + CA max/min
* AB + BC + CA max : quỹ tích của bài toán này là A, B, C tạo thành một tam giác đều.
Khi đó thì AB = BC = CA = sqrt(3)
Tức là ta cần tìm tập hợp các điểm A, B, C chạy trên đường tròn (O, 2) sao cho tam giác
ABC đều
* AB + BC + CA min : quỹ tích là A, B, C trùng nhau
Tức là ta cần tìm khoảng thời gian mà kim giờ, kim phút, kim giây trùng nhau(Thực tế
là chỉ kim giờ với kim phút trung nhau :3)
"""

def minimize_length():
    """
    Vận tốc kim giờ trên mặt đồng hồ: 360độ / 12giờ = 30độ / 3600giây = 1/120độ / giây
    Vận tốc kim phút trên mặt đồng hồ: 360độ / giờ = 1/10độ / giây
    """
    v_hours = 1/120
    v_minutes = 1/10
    # Khoảng thời gian để kim phút trùng kim giờ:
    duration = 360 / (1/10 - 1/120)
    # Thời gian hoạt động của đồng hồ: 11h59'50'' - 00h00'10''
    length = 11*3600 + 59*60 + 50 - 10
    print(length / duration)

def maximize_length():
    """
    Ta cần tìm khoảng thời gian mà kim giờ, kim phút tạo với nhau 1 góc = 120 độ
    Thực hiện tương tự như minimize_length()
    """