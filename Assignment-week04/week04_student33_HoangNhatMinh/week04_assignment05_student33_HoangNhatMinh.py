with open('additionalFolder\\MorseCode.txt') as mc:
    lines = mc.readlines()

toMorseCode = {}
toCharacter = {}
for line in lines:
    tmp = line.rstrip()
    tmp = tmp.split('\t')
    toMorseCode[tmp[0]] = tmp[1]
    toCharacter[tmp[1]] = tmp[0]

with open('additionalFolder\\week04_assignment05_data.txt') as mc:
    data = mc.readlines()

data = data[0].split(' ')
for i in range(len(data)):
    data[i] = toCharacter[data[i]]

result = ''.join(data) #ALLIWANTTOSAYISDOTDOTSPACEDOTDASHDOTDOTSPACEDASHDASHDASHSPACEDOTDOTDOTDASHSPACEDOTSPACEDASHDOTDASHDASHSPACEDASHDASHDASHSPACEDOTDOTDASH
result = result.replace('DOT', '.')
result = result.replace('DASH', '-')
result = result.replace('SPACE', ' ') #ALLIWANTTOSAYIS.. .DASH.. DASHDASHDASH ...DASH . DASH.DASHDASH DASHDASHDASH ..DASH
i = -1
for _ in result:
    i += 1
    if _ == '.': break
result = result[i:].split(' ')
for i in range(len(result)):
    result[i] = toCharacter[result[i]]
result = ''.join(result)
print(result)
# Ta cần gửi lại một đoạn mã khác để trả lời
# .-- .... . -. .-- .. .-.. .-.. .-- . --. . - -- .- .-. .-. .. . -.. ..--..


# https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/MorseDASHcodeDASHtree.svg/1000pxDASHMorseDASHcodeDASHtree.svg.png
