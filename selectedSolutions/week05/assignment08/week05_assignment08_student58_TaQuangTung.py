from pickletools import stringnl


print("Bài 8: Vietkey")

#Chuyển đổi ký tự tiếng việt sang tiếng anh
def vnm_to_eng(st):
    patterns = {
        'à': 'af', 'á': 'as', 'ả': 'ar', 'ã': 'ax', 'ạ': 'aj',
        'ă': 'aw', 'ằ': 'awf', 'ắ': 'aws', 'ẳ': 'awr', 'ẵ': 'awx', 'ặ': 'awj',
        'â': 'aa', 'ầ': 'aaf', 'ấ': 'aas', 'ẩ': 'aar', 'ẫ': 'aax', 'ậ': 'aaj',
        'đ': 'dd', 'ì': 'if', 'í': 'is', 'ỉ': 'ir', 'ĩ': 'ix', 'ị': 'ij',
        'è': 'ef', 'é': 'es', 'ẻ': 'er', 'ẽ': 'ex', 'ẹ': 'ej',
        'ê': 'ee', 'ề': 'eef', 'ế': 'ees', 'ể': 'eer', 'ễ': 'eex', 'ệ': 'eej',
        'ò': 'of', 'ó': 'os', 'ỏ': 'or', 'õ': 'ox', 'ọ': 'oj',
        'ô': 'oo', 'ồ': 'oof', 'ố': 'oos', 'ổ': 'oor', 'ỗ': 'oox', 'ộ': 'ooj',
        'ơ': 'ow', 'ờ': 'owf', 'ớ': 'ows', 'ở': 'owr', 'ỡ': 'owx', 'ợ': 'owj',
        'ù': 'uf', 'ú': 'us', 'ủ': 'ur', 'ũ': 'ux', 'ụ': 'uj',
        'ư': 'uw', 'ừ': 'uwf', 'ứ': 'uws', 'ử': 'uwr', 'ữ': 'uwx', 'ự': 'uwj',
        'ỳ': 'yf', 'ý': 'ys', 'ỷ': 'yr', 'ỹ': 'yx', 'ỵ': 'yj'
    }
    lst = []
    for i in st:
        lst.append(i)
    
    for ele in range(len(lst)):
        for key, val in patterns.items():
            if key == lst[ele]:
                lst[ele] = val
    stringle = ""
    for i in lst:
        stringle += i 
    print("eng =", stringle.strip())

#Chuyển đổi ký tự tiếng anh sang tiếng việt
def eng_to_vnm(stl):
    patterns = {
        'à': 'af', 'á': 'as', 'ả': 'ar', 'ã': 'ax', 'ạ': 'aj',
        'ă': 'aw', 'ằ': 'awf', 'ắ': 'aws', 'ẳ': 'awr', 'ẵ': 'awx', 'ặ': 'awj',
        'â': 'aa', 'ầ': 'aaf', 'ấ': 'aas', 'ẩ': 'aar', 'ẫ': 'aax', 'ậ': 'aaj',
        'đ': 'dd', 'ì': 'if', 'í': 'is', 'ỉ': 'ir', 'ĩ': 'ix', 'ị': 'ij',
        'è': 'ef', 'é': 'es', 'ẻ': 'er', 'ẽ': 'ex', 'ẹ': 'ej',
        'ê': 'ee', 'ề': 'eef', 'ế': 'ees', 'ể': 'eer', 'ễ': 'eex', 'ệ': 'eej',
        'ò': 'of', 'ó': 'os', 'ỏ': 'or', 'õ': 'ox', 'ọ': 'oj',
        'ô': 'oo', 'ồ': 'oof', 'ố': 'oos', 'ổ': 'oor', 'ỗ': 'oox', 'ộ': 'ooj',
        'ơ': 'ow', 'ờ': 'owf', 'ớ': 'ows', 'ở': 'owr', 'ỡ': 'owx', 'ợ': 'owj',
        'ù': 'uf', 'ú': 'us', 'ủ': 'ur', 'ũ': 'ux', 'ụ': 'uj',
        'ư': 'uw', 'ừ': 'uwf', 'ứ': 'uws', 'ử': 'uwr', 'ữ': 'uwx', 'ự': 'uwj',
        'ỳ': 'yf', 'ý': 'ys', 'ỷ': 'yr', 'ỹ': 'yx', 'ỵ': 'yj'
    }

    lt_key = []                 #Mảng chứa các phần tử theo key trùng với stl
    lt_value = []               #Mảng chứa các phần tử theo value trùng với stl
    for key, val in patterns.items():
        if val in stl:
            lt_key.append(key)
            lt_value.append(val)
    
    lt_key.reverse()
    lt_value.reverse()
    
    length = len(lt_value)

    if lt_key != [] and lt_value != []:
        for i in range(length):
            stl = stl.replace(lt_value[i], lt_key[i])
        print(f"vnm = {stl}")
    else:
        print(f"vnm = {stl}")


#Chuyển từ vnm sang eng
st = input("Nhập vnm: ")
vnm_to_eng(st)
print()

#Chuyển từ eng sang vnm
stl = input("Nhập eng: ")
eng_to_vnm(stl)
