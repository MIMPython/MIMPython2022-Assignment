paragraph = "Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities."

def isExist(key): #Kiểm tra xem từ khoá có tồn tại
    if key in paragraph:
        print (f"Từ khoá {key} có tồn tại trong đoạn văn")
    else:
        print (f"Từ khoá {key} không tồn tại trong đoạn văn")
        
def countKey(key): #Đếm số lần từ khoá xuất hiện
    print(f"Số lần xuất hiện từ khoá {key}: {paragraph.count(key,)}")
    
def countWords(): #Đếm số từ trong đoạn văn
    print(f"Số từ trong đoạn văn : {len(paragraph.split())}")
    
def formatParagraph(): #Viết lại đoạn văn, trong đó viết hoa tất cả các chữ trong câu đầu
    temp = paragraph.find(".")
    new = f"{paragraph[:temp].upper()}.{paragraph[temp+1:]}"
    return new

def main():
    #Câu a
    print ("Câu a:")
    isExist("Python") #Từ khoá Python có tồn tại trong đoạn văn
    isExist("contains") #Từ khoá contains không tồn tại trong đoạn văn
    isExist("experience") #Từ khoá experience có tồn tại trong đoạn văn
    isExist("difficult") #Từ khoá difficult không tồn tại trong đoạn văn
    #Câu b
    print (f"\nCâu b:")
    countKey("Python") #Số lần xuất hiện từ khoá Python: 5
    #Câu c
    print (f"\nCâu c:")
    countWords() #Số từ trong đoạn văn : 78
    #Câu d
    print (f"\nCâu d:")
    print (formatParagraph())

if __name__ == "__main__":
    main()
