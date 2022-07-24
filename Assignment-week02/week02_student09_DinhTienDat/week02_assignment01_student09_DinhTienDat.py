a = """
Bài tập 1:

	a) Quy tắc đặt tên biến:
		Khi đặt tên cho các biến trong python, chúng ta chỉ được phép 
		dùng chữ cái, số và dấu gạch dưới "_", chúng ta không được phép 
		nhấn space giữa các kí tự. Hơn nữa, tên của một biến có thể được
		bắt đầu bằng dấu gạch dưới hoặc bằng một chữ cái nhưng không được
		phép bắt đầu bằng chữ số.

	b) Một số ví dụ:
		- Tên biến không hợp lệ:
			+) 01_assignment
			+) bai tap 01
			+) "baitap01"
		- Tên biến hợp lệ:
			+) assignment_01
			+) bai_tap_01

	c) Khi nói về cách đặt tên biến, tác giả Robert C. Martin có viết trong 
	cuốn sách Clean Code: A Handbook of Agile Software Craftsmanship rằng:

	It is easy to say that names should reveal intent. What we want to impress 
	upon you is that we are serious about this. Choosing good names takes time 
	but saves more than it takes. So take care with your names and change them
	when you find better ones. Everyone who reads your code (including you) will
	be happier if you do.
	The name of a variable should answer all the big questions. It should tell you 
	why it exists, what it does, and how it is used. If a name requires a comment,
	then the name does not reveal its intent.

	với nhắn nhủ rằng chúng ta nên đặt tên biến hợp lệ và càng cụ thể càng tốt nhưng
	cũng không quá dài hay không quá ngắn. Một ví dụ mà em nghĩ ra trong tình huống 
	này là:
	Ví dụ như chúng ta muốn đặt tên cho một biến mô tả điểm của một sinh viên tên A:
		- Cách đặt không hợp lí: 
			+) so_diem_cua_sinh_vien_A (quá dài)
			+) dsvA (quá vắn tắt)
			+) diem sv A (không hợp lệ)

		- Cách đặt hợp lí: diem_sv_A

	d) Sau đây là danh sách những tên biến có cùng ý nghĩa thể hiện số sinh viên và 
	bình luận về cách đặt tên ấy như sau:
		+) numberofcollegestudents (các kí tự được viết sát nhau,không có khoảng cách)
		+) NUMBEROFCOLLEGESTUDENTS (các kí tự được viết hoa, viết sát nhau và không
		có khoảng cách)
		+) numberOfCollegeStudents (các kí tự được viết sát nhau, những từ sau từ đầu
		tiên được viết hoa chữ cái đầu tiên)
		+) NumberOfCollegeStudents (các kí tự được viết sát nhau, tất cả các từ đều
		được viết hoa chữ cái ban đầu)
		+) number_of_college_students (các từ đều được viết thường, không viết hoa và
		được tách ra bởi dấu gạch dưới thay cho kí tự space)

	e) Một số phong cách đặt tên biến phổ biến hiện nay:
		+) Camel Case: tất cả các từ sau từ đầu tiên đều được viết hoa chữ cái đầu,
		cách viết số ba của ý d) chính là một ví dụ cho phong cách này.
		+) Pascal Case: tất cả các từ đều được viết hoa chữ cái đầu tiên, cách viết số 
		bốn của ý d) chính là một ví dụ cho phong cách này.
		+) Snake Case: tất cả các từ đều được viết thường, không viết hoa, các từ được
		phân cách nhau bởi dấu gạch dưới thay cho kí tự space, cách viết số năm của ý d)
		chính là một ví dụ cho phong cách này.

	f) Khi viết một đoạn Code, em sẽ ưu tiên Snake Case đầu tiên bởi tính rõ ràng và dễ 
	đọc của nó.

"""
print(a)