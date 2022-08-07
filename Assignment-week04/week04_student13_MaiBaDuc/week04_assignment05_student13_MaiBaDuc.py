morse = []
morse_1 = []
count=0
s1=''
s2=''
with open('morse.txt') as file_object:  #luu ma morse trong file morse.txt
    for line in file_object:
        line = line.strip()
        s1, s2= line.split(' ')
        morse.append(s1) #list ki tu
        morse_1.append(s2) #list ki hieu
sample = '.- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ....'
example = []
result = ""
for i in sample.split(" "):
    for j in morse_1:
        if i==j: 
            result=result+morse[morse_1.index(j)]

print(result)

# print(len(morse))
# print(len(morse_1))