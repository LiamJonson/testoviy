a,b = map(int, input().split('/'))
k =[]
while b != 0:
    l = b
    a,b =divmod(a,b)
    k.append(a)
    a = l
print(*k)
