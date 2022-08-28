# Dictionary1 ={
#     "á":"a",
#     "à":"a",
#     "ã":"a",
#     "ạ":"a",
    
#     "ă":"aw",
#     "ắ":"aw",
#     "ắ":"aw",
#     "ẵ":"aw",
#     "ằ":"aw",
    
#     "â":"aa",
#     "ấ":"aa",
#     "ầ":"aa",
#     "ẫ":"aa",
#     "ậ":"aa",
    
#     "đ":"dd",
    
#     "é":"e",
#     "è":"e",
#     "ẽ":"a",
#     "ẹ":"a",
    
#     "ê":"ee",
#     "ế":"ee",
#     "ề":"ee",
#     "ễ":"ee",
#     "ệ":"ee",
    
#     "í":"i",
#     "ì":"i",
#     "ĩ":"i",
#     "ị":"i",
    
#     "ó":"o",
#     "ò":"o",
#     "õ":"o",
#     "ọ":"o",
    
#     "ô":"oo",
#     "ố":"oo",
#     "ồ":"oo",
#     "ỗ":"oo",
#     "ộ":"oo",
    
#     "ớ":"ow",
#     "ờ":"ow",
#     "ỡ":"ow",
#     "ợ":"ow",
    
#     "ú":"u",
#     "ù":"u",
#     "ũ":"u",
#     "ụ":"u",
    
#     "ư":"uw",
#     "ứ":"uw",
#     "ừ":"uw",
#     "ữ":"uw",
#     "ự":"uw",
    
#     "ý":"y",
#     "ỳ":"y",
#     "ỹ":"y",
#     "ỵ":"y",
# }

# # ......................
# Dictionary2 ={
#     "á":"s",
#     "à":"f",
#     "ã":"x",
#     "ạ":"j",
    
#     "ă":"",
#     "ắ":"s",
#     "ắ":"f",
#     "ẵ":"x",
#     "ằ":"j",
    
#     "â":"",
#     "ấ":"s",
#     "ầ":"f",
#     "ẫ":"x",
#     "ậ":"j",

#     "đ":"",
    
#     "é":"s",
#     "è":"f",
#     "ẽ":"x",
#     "ẹ":"j",
    
#     "ê":"",
#     "ế":"s",
#     "ề":"f",
#     "ễ":"x",
#     "ệ":"j",
    
#     "í":"s",
#     "ì":"f",
#     "ĩ":"x",
#     "ị":"j",
    
#     "ó":"s",
#     "ò":"f",
#     "õ":"x",
#     "ọ":"j",
    
#     "ô":"",
#     "ố":"s",
#     "ồ":"f",
#     "ỗ":"x",
#     "ộ":"j",
    
#     "ơ":"",
#     "ớ":"s",
#     "ờ":"f",
#     "ỡ":"x",
#     "ợ":"j",
    
#     "ú":"s",
#     "ù":"f",
#     "ũ":"x",
#     "ụ":"j",
    
#     "ư":"",
#     "ứ":"s",
#     "ừ":"f",
#     "ữ":"x",
#     "ự":"j",
    
#     "ý":"s",
#     "ỳ":"f",
#     "ỹ":"x",
#     "ỵ":"j",
# }

# B=str("")
# A=str(input())
# A=A.lower()
# for i in A:
#     if(ord(i)<122):
#         B+=i
#     else :
#         B+=Dictionary1[i]+Dictionary2[i]
# print(B)

# # ..........................................
Dictionary1 ={
    "as":"á",
    "af":"à",
    "ax":"ã",
    "aj":"ạ",
    
    "aw":"ă",
    "aws":"ắ",
    "awj":"ặ",
    "awx":"ẵ",
    "awf":"ằ",
    
    "aa":"â",
    "aas":"ấ",
    "aaf":"ầ",
    "aax":"ẫ",
    "aaj":"ậ",
    
    "dd":"đ",
    
    "es":"é",
    "ef":"è",
    "ex":"ẽ",
    "ẹ":"ẹ",
    
    "ee":"ê",
    "ees":"ế",
    "eef":"ề",
    "eex":"ễ",
    "eej":"ệ",
    
    "is":"í",
    "if":"ì",
    "ix":"ĩ",
    "ij":"ị",
    
    "os":"ó",
    "of":"ò",
    "ox":"õ",
    "oj":"ọ",
    
    "oo":"ô",
    "oos":"ố",
    "oof":"ồ",
    "oox":"ỗ",
    "ooj":"ộ",
    
    "ow":"ơ",
    "ows":"ớ",
    "owf":"ờ",
    "owx":"ỡ",
    "owj":"ợ",
    
    "us":"ú",
    "uf":"ù",
    "ux":"ũ",
    "uj":"ụ",
    
    "uw":"ư",
    "uws":"ứ",
    "uwf":"ừ",
    "uwx":"ữ",
    "uwj":"ự",
    
    "ys":"ý",
    "yf":"ỳ",
    "yx":"ỹ",
    "yj":"ỵ",
}

# ......................
Dictionary2 ={
    "as":"á",
    "af":"à",
    "ax":"ã",
    "aj":"ạ",
    
    "ă":"",
    "aws":"ắ",
    "awf":"ằ",
    "awx":"ẵ",
    "awj":"ặ",
    
    "â":"",
    "aas":"ấ",
    "aaf":"ầ",
    "ẫ":"x",
    "ậ":"j",

    "đ":"",
    
    "é":"s",
    "è":"f",
    "ẽ":"x",
    "ẹ":"j",
    
    "ê":"",
    "ế":"s",
    "ề":"f",
    "ễ":"x",
    "ệ":"j",
    
    "í":"s",
    "ì":"f",
    "ĩ":"x",
    "ị":"j",
    
    "ó":"s",
    "ò":"f",
    "õ":"x",
    "ọ":"j",
    
    "ô":"",
    "ố":"s",
    "ồ":"f",
    "ỗ":"x",
    "ộ":"j",
    
    "ơ":"",
    "ớ":"s",
    "ờ":"f",
    "ỡ":"x",
    "ợ":"j",
    
    "ú":"s",
    "ù":"f",
    "ũ":"x",
    "ụ":"j",
    
    "ư":"",
    "ứ":"s",
    "ừ":"f",
    "ữ":"x",
    "ự":"j",
    
    "ý":"s",
    "ỳ":"f",
    "ỹ":"x",
    "ỵ":"j",
}

B=str("")
A=str(input())
A=A.lower()
for i in A:
    if(ord(i)<122):
        B+=i
    else :
        B+=Dictionary1[i]+Dictionary2[i]
print(B)