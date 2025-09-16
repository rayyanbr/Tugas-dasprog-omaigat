n, k = map(int, input().split())
a = list(map(int, input().split()))
bisa_dibeli = 0
for harga in a:
    if harga <= k:
        bisa_dibeli += 1
print(bisa_dibeli)