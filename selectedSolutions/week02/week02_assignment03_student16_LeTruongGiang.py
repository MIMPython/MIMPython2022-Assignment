
def fileName():
    print("Nhập tên: ", end='')
    name = str(input())
    title_name = name.title()
    trans = name.maketrans("áàảãạăắằẳẵặúùủũụưứừửữựêếềểễệéèẻẽẹóòỏõọôốồổỗộớờơởỡợíìỉĩịýỳỷỹỵÁÀẢÃẠĂẮẰẲẴẶÚÙỦŨỤƯỨỪỬỮỰÊẾỀỂỄỆÉÈẺẼẸÓÒỎÕỌÔỐỒỔỖỘỚỜƠỞỠỢÍÌỈĨỊÝỲỶỸỴĐ","aaaaaaaaaaauuuuuuuuuuueeeeeeeeeeeoooooooooooooooooiiiiiyyyyyAAAAAAAAAAAUUUUUUUUUUUEEEEEEEEEEEOOOOOOOOOOOOOOOOOIIIIIYYYYYD")
    new_name = title_name.translate(trans)
    out_name = new_name.replace(" ", "")

    print("Nhập tuần: ", end='')
    week = int(input())
    print("Nhập số thứ tự bài tập: ", end='')
    assignment = int(input())
    
    if assignment < 10:
        if week < 10:
            return 'week0' + str(week) + '_' + 'assignment0' + str(assignment) + '_' + out_name + '.py'
        else:
            return 'week' + str(week) + '_' + 'assignment0' + str(assignment) + '_' + out_name + '.py'
    else:
        if week < 10:
            return 'week0' + str(week) + '_' + 'assignment' + str(assignment) + '_' + out_name + '.py'
        else:
            return 'week' + str(week) + '_' + 'assignment' + str(assignment) + '_' + out_name + '.py'
    
print(fileName())
    

     