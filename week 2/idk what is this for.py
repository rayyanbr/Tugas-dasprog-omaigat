n = int(input())
result = []
for i in range(n):
    word = input()
    if len(word) > 10:
        result.append(word[0] + str(len(word) - 2) + word[-1])
    else:
        result.append(word)
for words in result:
    print(words)