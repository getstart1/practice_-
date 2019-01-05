import sys
while True:
    try:
        num = int(sys.stdin.readline().strip())
        num.reverse()
        num = num[::-1]
        print(num)

    except:
        break
