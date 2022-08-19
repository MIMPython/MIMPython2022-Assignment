"""
Để xem chi tiết giải thích thì hãy xem trong folder Ex9 ở mục additionaFolder
"""

import math

def convert(number):
    return number<10 and "0"+str(number) or str(number)

def time(hour,minute,second):
    hour,minute,second =convert(hour),convert(minute),convert(second)
    return "{}:{}:{}".format(hour,minute,second)

def correctTime(h,m,s):        
    m += s//60
    h += m//60
    s %= 60
    m %= 60
    h %= 24
    return h,m,s

def lastTime(h,m,s):
    if h>=11:
        if m>=59:
            if s>=50:
                return False
    return True

def degreeByTime(h,m,s):
    hD,mD,sD = 0,0,0
    sD += s*6
    mD += m*6
    hD += h*30 + (m//12)*6
    return hD,mD,sD

def toRad(degree):
    return degree*math.pi/180

# This method caculate cosin by degree and make code shorter
def cos(degree):
    return math.cos(toRad(degree))

def distance(first,last):
    angle = abs(last-first)
    angle = angle>180  and 360-angle or angle
    return(2-2*cos(angle))**(1/2)

def caculateM(h,m,s):
    aob,aoc,boc = degreeByTime(h,m,s)
    M = distance(aob,aoc) + distance(aoc,boc) + distance(aob,boc)
    return M

if __name__ == "__main__":
    h,m,s = 0,0,10
    maxM,minM = -1,6
    timeMaxs,timeMins = [],[]
    while lastTime(h,m,s):
        M = caculateM(h,m,s)
        if M < minM:
            timeMins.clear()
            minM = M
        elif M > maxM:
            timeMaxs.clear()
            maxM = M
        if M == maxM:
            timeMaxs.append(time(h,m,s))
        elif M == minM:
            timeMins.append(time(h,m,s))
        s+=1
        h,m,s = correctTime(h,m,s)

    
    print("Max of M is:",maxM)
    print("M max at time:\n",timeMaxs)
    print("\n")
    print("Min of M is:",minM)
    print("M min at time:\n",timeMins)

