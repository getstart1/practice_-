#convert 16进制到10进制
while True:
    try:
        n=raw_input()
        r=int(n,16)
        print r
    except:
        break


# import sys
#
#
# while True:
#     try:
#         ten_result = 0
#         list = []
#         sixteen_n= (sys.stdin.readline().strip())
#         l = len(sixteen_n)
#         for i in range(l):
#             if (sixteen_n[i] == 'A'):
#                 list.append(10)
#             elif (sixteen_n[i] == 'B'):
#                 list.append(11)
#             elif (sixteen_n[i] == 'C'):
#                 list.append(12)
#             elif (sixteen_n[i] == 'D'):
#                 list.append(13)
#             elif (sixteen_n[i] == 'E'):
#                 list.append(14)
#             elif (sixteen_n[i] == 'F'):
#                 list.append(15)
#             elif (sixteen_n[i] == 'x'):
#                 list.append(0)
#             else:
#                 list.append(int(sixteen_n[i]))
#         for i in range(l):
#             ten_result = ten_result + list[i]* pow(16,(l-i-1))
#         print(ten_result)
#
#     except:
#         break
