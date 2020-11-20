
x = 'Norma, Anja'
y = 'Alexandra, Roma, Jettie, Phung, Daron'
print(*[i for i in set(y.split(', ')).union(x.split(', '))],sep=', ')
#print(*x+y,sep =', ')