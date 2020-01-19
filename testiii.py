units = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1.0, 'cm': 0.01, 'mm': 0.001}
v = input().split(' ')
print(v)
k = (float(v[0]) * units[v[1]] / units[v[3]])
print(k)
print('{:.4E}'.format(k))
#print('%.2e'%(k))
#print(a)

