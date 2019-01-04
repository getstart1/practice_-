#Count the length of the last word in a string
#https://www.nowcoder.com/practice/8c949ea5f36f422594b306a2300315da?tpId=37&tqId=21224&tPage=1&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
string = input()
for i in range(len(string)):
    if (string[len(string)- i -1] != ' '):
        count = i + 1
    else:
        count = i
        break
print(count)
