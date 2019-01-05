#合并相同key的表
#link: https://www.nowcoder.com/practice/de044e89123f4a7482bd2b214a685201?tpId=37&tqId=21231&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking
import sys
while True:
    try:
        n = int(sys.stdin.readline().strip())
        result = {}
        for i in range(n):
            key, value = map(int, sys.stdin.readline().split(' '))
            result[key] = result.setdefault(key,0) + value
        for j in sorted(result.keys()):
            print(j, result[j])

    except:
        break
