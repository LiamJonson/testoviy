n = input().split()
kol = {}
for i in n:
    if len(i) in kol:
        kol[len(i)] +=1
    else:
        kol[len(i)] = 1
for i in sorted(kol):
    print(str(i) + ':' + str(kol[i]))

