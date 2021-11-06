from collections import deque
a=24
print(bin(a)[2:])
ls=deque()
while True:
    if a%2==0:ls.appendleft('0')
    else:ls.appendleft('1')
    a=a/2
    if a<=1:break
ls=('').join(ls)
print(ls)
