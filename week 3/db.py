import math

n = int(input())
numbers = []
results = []

for i in range(n):
    q = int(input())
    numbers.append(q)

for q in numbers:
    lim = math.isqrt(q)
    found = False
    for a in range(1, lim + 1):
        for b in range(1, lim + 1):
            for c in range(1, lim + 1):
                for d in range(1, lim + 1):
                    if a*a + b*b + c*c + d*d == q:
                        found = True
                        break
                if found: break
            if found: break
        if found: break
    results.append("LEAVE" if found else "ERASE")
for res in results:
    print(res)
    