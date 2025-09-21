n, m, k = map(int, input().split())
a = list(map(int, input().split()))
total_energy = 0
for i in range(k):
    x, y = map(int, input().split())
    energy = 0
    for i in range(x-1, y-1):
        energy += a[i]
    total_energy += energy
if total_energy <= m:
    print(f"EZ banget, energiku sisa {m - total_energy}!")
else:
    print(f"NT, kurang {total_energy - m} energi sih.")