from math import inf

def f(x):
    return ((2 * x ** 2) - (3 * x) - 5) / ((3 * x ** 2) + x + 1)

x0= 0
dx_list = [1e6, -1e6]
for dx in dx_list:
    print((round(f(x0+dx),3)))




