def check(a,b,c,d,e,f,g,h,i):
    return a + b / c + d + e / f == g + h / i

def solve():
    lst = []
    for a in range(1,10):
        for b in range(1,10):
            if b == a: continue
            for c in range(1,10): 
                if c in (a, b): continue
                for d in range(1,10):
                    if d in (a, b, c): continue
                    for e in range(1,10):
                        if e in (a, b, c, d): continue
                        for f in range(1,10):
                            if f in (a, b, c, d ,e): continue
                            for g in range(1,10):
                                if g in (a, b, c, d, e, f): continue
                                for h in range(1,10):
                                    if h in (a, b, c, d, e, f, g): continue
                                    for i in range(1,10):
                                        if i in (a, b, c, d, e, f, g, h): continue
                                        if check(a,b,c,d,e,f,g,h,i):
                                            lst.append([a,b,c,d,e,f,g,h,i])
    return lst

lst = solve()
print("Amount numbers that vaild is:" , len(lst))