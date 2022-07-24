alphabet = 'abcdefghijklmnopqrstuvwxyz'
def ma_hoa(word):
    res=''
    for i in range(len(word)):
        for j in range(len(alphabet)):
            if word[i]==alphabet[j]:
                res += alphabet[j-13]

    return res

def giai_ma(word):
    res=''
    for i in range(len(word)):
        for j in range(len(alphabet)):
            if word[i]==alphabet[j]:
                res += alphabet[j+13-26]
    return res

print(ma_hoa('huyen'))  
print(giai_ma('uryyb'))