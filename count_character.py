#计算字符个数
#https://www.nowcoder.com/practice/a35ce98431874e3a820dbe4b2d0508b1?tpId=37&tqId=21225&tPage=1&rp=&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking
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
