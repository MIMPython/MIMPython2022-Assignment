lst = []

for A in range(1, 10):
    for B in range(1, 10):
        for C in range(1, 10):
            for D in range(1, 10):
                for E in range(1, 10):
                    for F in range(1, 10):
                        for G in range(1, 10):
                            for H in range(1, 10):
                                for I in range(1, 10):
                                    if (A + B / C + D + E / F == G + H / I) and (A != B) and (A != C) and (A != D) and \
                                            (A != E) and (A != F) and (A != G) and (A != H) and (A != I) and (
                                            B != C) and \
                                            (B != D) and (B != E) and (B != F) and (B != G) and (B != H) and (
                                            B != I) and \
                                            (C != D) and (C != E) and (C != F) and (C != G) and (C != H) and (
                                            C != I) and \
                                            (D != E) and (D != F) and (D != G) and (D != H) and (D != I) and (
                                            E != F) and \
                                            (E != G) and (E != H) and (E != I) and (F != G) and (F != H) and (
                                            F != I) and \
                                            (G != H) and (G != I) and (H != I):
                                        result = 'A: ' + str(A) + ', B: ' + str(B) + ', C: ' + str(C) + ', D: ' + str(D) \
                                                 + ', E: ' + str(E) + ', F:: ' + str(F) + ', G: ' + str(G) \
                                                 + ', H: ' + str(H) + ', I: ' + str(I)
                                        lst.append(result)

print(lst)  # 180 outcome

