import math

# x,y = (int(x) for x in input().split())
x,y = map(int, input().split())

if y <= x:
    print(0)
else:
    print(math.ceil((y-x) / 10))