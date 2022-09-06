'''
Bài tập 1. (list average)
Viết một hàm nhận vào một list và trả về giá trị trung bình của danh sách đó. Đặt thêm cấu trúc try-except để thông báo khi nhận được một list rỗng. Bắt thêm các lỗi khác nếu có.
'''

def getAverageOfList(list):

    try:
        averageOfList = sum(list)/len(list)
    except ZeroDivisionError:
            print('List is null !')          
    else: 
        print(averageOfList)           

if __name__ == '__main__':
    list = [] 
    getAverageOfList(list) # List is null !