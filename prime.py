#将一个数字分解成质数的乘积
import sys
from math import sqrt, floor

n = int(raw_input())
m = int(floor(sqrt(n) + 0.5))
print('value of m is', m)
for i in range(2, m + 1):
    while n % i == 0:
        sys.stdout.write(str(i) + ' ')
        n /= i
if n != 1:
    sys.stdout.write(str(n) + ' ')
