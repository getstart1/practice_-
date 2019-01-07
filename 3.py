import sys
while True:
    try:
        info = sys.stdin.readline().strip().split(' ')
        box_info = info[0].split(',')
        length = int(box_info[0])
        height = int(box_info[1])

        start_info = info[1].split(',')
        start_x = int(start_info[0])
        start_y = int(start_info[1])

        end_info = info[2].split(',')
        end_x = int(end_info[0])
        end_y = int(end_info[0])

        block_n = info[3]
        #print(info)



    except:
        break
