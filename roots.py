def findRoots(A, B, C):
    D = B**2 - 4*A*C
    if D >= 0:
        r1 = (-B-D**(0.5))/(2*A)
        if D == 0:
            R = [r1]
        else:
            r2 = (-B+D**(0.5))/(2*A)
            if A > 0:
                R = [r1, r2]
            else:
                R = [r2, r1]
    else:
        R = [-1]
    return R   
