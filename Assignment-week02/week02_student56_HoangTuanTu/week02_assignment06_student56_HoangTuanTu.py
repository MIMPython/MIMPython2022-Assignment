from sre_parse import expand_template


def delta(a,b,c):
    return b*b - 4*a*c

def solve(a,b,c):
    dela = delta(a,b,c)
    
    if a==0:
        return "Not a Valid Quadratic equation"
    elif dela>0:
        x1=(-b-dela**(1/2))/(2*a)
        x2=(-b+dela**(1/2))/(2*a)
        experiment = (min(x1,x2),max(x1,x2))
        return experiment
    elif dela == 0:
        return (-b/2*a,)
    else:
        return ()

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve(1, 1, -2))
    print(solve(1, 2, 1)) 
    print(solve(1, 0, 1)) 

    experiments = solve(a,b,c)

    if (type(experiments) == tuple):
        aString = ""
        bString = ""
        cString = ""

        if abs(a)!=1:
            aString +=str(a)
        elif a<0:
            aString = "- "
        aString+="x^2"

        if b!=0:
            sign = ""
            if b<0:
                sign= " - "
            elif b>0:
                sign= " + "
            if abs(b)!=1:  
                bString = sign+str(abs(b))+"x"
            else:
                bString = sign+"x"

        if c!=0:
            sign = ""
            if c>0:
                sign= " + "
            else:
                sign= " - "
            cString =sign+str(abs(c))
            
        print("Equation {}{}{} = 0 have experiment:".format(aString, bString ,cString),end=" ")
    print(experiments)
    
