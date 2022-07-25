#Bai6

def giaipt(a,b,c):
    answer = ()
    if a == 0:
        if b==0: 
            if c==0:
                pass
        else:
            answer = (-c/b,)
    else:
        delta = b**2 - 4*a*c   
        if delta > 0: 
            answer = ((-b - delta**(1/2))/(2*a),(-b + delta**(1/2))/(2*a))
        elif delta < 0:
            pass
        else:
            answer = ( -b/(2*a))         
    return answer

print(giaipt(3,-2,-1)) #(-0.3333333333333333, 1.0)
print(giaipt(5,2,-10)) #(-1.6282856857085701, 1.22828568570857)
print(giaipt(3,4,5)) #()

    