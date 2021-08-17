import math
size = int(input())
H = [int(i) for i in input().split()]
u = []

def sitfdown(i):
    minIndex = i
    l = 2 * i + 1
    if l <= size-1 and H[l] < H[minIndex]:
        minIndex = l
    z = 2 * i + 2
    if z <= size-1 and H[z] < H[minIndex]:
        minIndex = z
    if i != minIndex:
        H[i],H[minIndex] = H[minIndex],H[i]
        u.append([i,minIndex])
        sitfdown(minIndex)

k = [int(i) for i in range(0,math.ceil(size/2))]
for i in reversed(k):
    sitfdown(i)

if not u:
    print(0)
else:
    print(len(u))
    for i in u:
        print(*i)