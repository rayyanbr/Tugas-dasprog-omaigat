import math

n = int(input())
numbers = []
for i in range(n):
    q = int(input())
    lim = math.isqrt(q)
    found = False
    for a in range(lim + 1):
        for b in range(lim + 1):
            for c in range(lim + 1):
                for d in range(lim + 1):
                    if a*a + b*b + c*c + d*d == q:
                        found = True
                        break
                if found: break
            if found: break
        if found: break
    print("LEAVE" if found else "ERASE")
