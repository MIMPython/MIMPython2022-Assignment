import maskpass
# a; b)
print ("Player A please enter: Keo, Bua, Bao")
playerA = maskpass.askpass(prompt="", mask="*")
print ("Player B please enter: Keo, Bua, Bao")
playerB = maskpass.askpass(prompt="", mask="*")

a = ["Keo", "Bua", "Bao"]

if (playerA not in a) or (playerB not in a):
    print ("You entered wrong")
elif playerA == playerB:
    print (f"Player A: {playerA} - {playerB} :Player B" )
    print ("Draw")
elif ((playerA == "Keo" and playerB == "Bua") or 
      (playerA == "Bua" and playerB == "Bao") or 
      (playerA == "Bao" and playerB == "Keo")):
    print (f"Player A: {playerA} - {playerB} :Player B" )
    print ("Player B win")
else:
    print (f"Player A: {playerA} - {playerB} :Player B" )
    print ("Player A win") 

# c) Giả sử A là người đi trước, còn B là người đi sau
# Có thể hiểu tích công bằng là người chơi B không biết được người chơi A lựa chọn Kéo, Búa hay Bao









