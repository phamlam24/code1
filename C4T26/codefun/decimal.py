import math
a = int(input())
b = int(input())
c = a/b
d = math.modf(c)
e = d[0] *(10**72)
f = str(e)
print(f[70])