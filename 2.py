import sys

while True:
    try:
        str = sys.stdin.readline().strip()
        n = int(raw_input())
        list = str.split(';')
        print(list)
        l = len(list)

        if (n <= (l - 1) and n >= 0) :
            result = list[n]
        else:
            result = ''
        print(result)

    except:
        break
