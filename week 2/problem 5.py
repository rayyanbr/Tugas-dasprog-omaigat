n = int(input())
storage = {}
cart = []
for i in range (n):
    items, qty = input().split()
    qty = int(qty)
    storage[items] = qty
n_c = int(input())
for i in range(n_c):
    c_items, c_qty = input().split()
    c_qty = int(c_qty)
    if c_items in storage:
        storage[c_items] -= c_qty
        cart.append(c_items)
print("CHARLIE")
print(", ".join(cart))
print("STORAGE")
for item, qty in storage.items():
    print(f"{item} : {qty}")