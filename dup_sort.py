import sys

while TRUE:
    try:
        list = []
        n = int(sys.stdin.readline().strip())

        for i in range(n):
            a = int(sys.stdin.readline().strip())
            list.append(a)
        new_list = sorted(set(list))
        for i in new_list:
            print i
    except:
        break



#delete duplicate number and sort
