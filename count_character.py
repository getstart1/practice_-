import sys
strList = []
count = 0
for line in sys.stdin:
    tempStr = line.split()
    strList.extend(tempStr)
string = strList[0]
#new_string = string[1:]
target = strList[1]
#new_target = target[:(len(target)-1)]
for i in range(0, len(string)):
    if (string[i].lower() == target or string[i].upper() == target):
        count = count + 1
print(count)
