bangMa={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
'--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
'--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S',
'-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z',
'-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5',
'-....':'6','--...':'7','---..':'8','----.':'9'}

maMorse = ".- .-.. .-.. .. .-- .- -. - - --- ... .- -.-- .. ... -.. --- - -.. --- - ... .--. .- -.-. . -.. --- - -.. .- ... .... -.. --- - -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. --- - -.. .- ... .... ... .--. .- -.-. . -.. --- - ... .--. .- -.-. . -.. .- ... .... -.. --- - -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. .- ... .... -.. .- ... .... -.. .- ... .... ... .--. .- -.-. . -.. --- - -.. --- - -.. .- ... ...."
tachChu = maMorse.split()
for i in range(0,len(tachChu)):
    print(bangMa.get(tachChu[i]), end=' ')