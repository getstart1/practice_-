string = input()
for i in range(len(string)):
    if (string[len(string)- i -1] != ' '):
        count = i + 1
    else:
        count = i
        break
print(count)
