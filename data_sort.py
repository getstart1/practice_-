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
