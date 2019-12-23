n = list(map(int, input().split()))
s = n
k = []
for i in range(len(n)-1):
    g = (s[0]-s[1])
    m = g if g > 0 else -g
    k.append(m)
    s.pop(0)
h = set(i for i in range(1, len(k)+1))
if set(k) == set(h):
    print('Jolly')
else:
    print('Not jolly')