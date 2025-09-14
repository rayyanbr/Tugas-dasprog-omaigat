d = int(input())
encrypted = []
for i in range(d):
    sn = int(input())
    m = input()
    shift_total = ""
    for char in m:
        if 'a' <= char <= 'z':
            shift = (ord(char) - ord('a') + sn) % 26 + ord('a')
            shift_total += chr(shift)
        elif 'A' <= char <= 'Z':
            shift = (ord(char) - ord('A') + sn) % 26 + ord('A')
            shift_total += chr(shift)
        else:
            shift_total += char
    encrypted.append(shift_total)
for enc in encrypted:
    print(enc)