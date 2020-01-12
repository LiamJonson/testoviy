a,b = map(int, input().split())
n = list(zip(*[input().split() for i in range(a)]))
for i in n:
    print(*i)




