
# Bài tập 1. (list average)
# Viết một hàm nhận vào một list và trả về giá trị trung bình của danh sách đó. 
# Đặt thêm cấu trúc try-except để thông báo khi nhận được một list rỗng. Bắt thêm các lỗi khác nếu có.

def list_average(list_numbers):
    try:
        if type(list_numbers) != list:
            return f"Input không phải 1 list."

        mean_list_numbers = sum(list_numbers) / len(list_numbers)
        return mean_list_numbers

    except ZeroDivisionError:
        return f"List của bạn không chứa phần tử nào."

    except TypeError:
        return f"Tồn tại 1 phần tử trong list không phải số."

    

if __name__ == "__main__":
    list_average([1,2,3,4]) #2.5
    list_average([1,2,'12']) #Tồn tại 1 phần tử trong list không phải số.
    list_average([]) #List của bạn không chứa phần tử nào.
    print(list_average((1,2,2,3))) #List của bạn không chứa phần tử nào.








