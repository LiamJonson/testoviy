n = input()
sl = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
      1000: 'M'}
k = []
def ost(x):
    er = 0
    h= x
    for j in sl.keys():
        if h in sl:
            print(sl[h], end='')
            break
        elif h >j and h > 1000:
            print(sl[1000]*int(str(h)[0]),end='')
            break
        elif h > j:
            er = j
        else:
            print(sl[er], end='')
            ost(h - er)
            break
p = 0
for i in n:
    k.append(int(i + '0' * (len(range(p, len(n) - 1)))))
    p+=1
for i in k:
    if i in sl:
        print(sl[i], end='')
    elif i == 0:
        continue
    else:
        ost(i)


