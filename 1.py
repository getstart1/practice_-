import sys
while True:
    try:
        input = raw_input()
        n = int(input)
        temp = 0
        l = len(input)
        i = 0

        if (l < 3 or l == 3):
            result = input

        else:
            for i in range(l - 2):
                new = int(input[i])* 100 + int(input[i+1])* 10 + int(input[i+2])*1
                if(new > temp):
                    temp = new
            result = str(temp)
        print(result)

    except:
        break
