print("Xin chào, đây là chương trình mã hoá ROT13")
print("Nhập văn bản mà bạn muốn mã hoá:")

def ceasar_rot13(phrase):
	bang_chu_cai = "abcdefghijklmnopqrstuvwxyz"
	rot13_phrase = ""

	for char in phrase:
		rot13_phrase += bang_chu_cai[(bang_chu_cai.find(char)+13)%26]
	return rot13_phrase

phrase = input()
print(ceasar_rot13(phrase))

print("Bây giờ, hãy nhập một đoạn mã, tôi sẽ giải nó cho bạn:")

def decode(phrase):
	bang_chu_cai = "abcdefghijklmnopqrstuvwxyz"
	decode_phrase = ""

	for char in phrase:
		decode_phrase += bang_chu_cai[(bang_chu_cai.find(char)-13)%26]
	return decode_phrase

phrase = input()
print(decode(phrase))