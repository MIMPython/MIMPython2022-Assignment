# Bài tập 3. Viết một hàm nhận vào tên học viên (kiểu string), số thứ tự tuần học (kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.
def assignment(name, week, assign):
    new_file_name = f"week{week}_assignment{assign}_{name}"
    f = open(new_file_name, "x")
    f.close()