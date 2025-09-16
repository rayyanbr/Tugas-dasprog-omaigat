n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for harga in a:
    if harga <= k:
        count += 1
print(count)