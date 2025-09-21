def subsums_equation(arr):
    n = len(arr)
    sub_arr = [0] * (n + 1)
    for i in range(n):
        sub_arr[i + 1] = sub_arr[i] + arr[i]
    return sub_arr
def subsum_range(sub_arr, l, r):
    return sub_arr[r + 1] - sub_arr[l]

n = int(input())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
subsumsA = subsums_equation(arr_A)
subsumsB = subsums_equation(arr_B)
t = int(input())
results = []
for i in range(t):
    l, r = map(int, input().split())
    sumresA = subsum_range(subsumsA, l, r)
    sumresB = subsum_range(subsumsB, l, r)
    if sumresA == sumresB:
        results.append("YA")
    else:
        results.append("TIDAK")
for i in results:
    print(i)