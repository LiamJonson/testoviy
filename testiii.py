def kaprekar(n, base=10):
    def convert(num, to_base=10, from_base=10):
        n = int(str(num), base=from_base)
        c = ''
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while n:
            c = alphabet[n % to_base] + c
            n //= to_base
        return c
    h = int(str(n),base=base)
    k = h ** 2
    g =convert(k,base)
    for i in range(1,len(str(g))):
        a,b = int(str(g[:i]),base),int(str(g[i:]),base)
        if a*b and a+b == h:
            return True
    return False

test_1 = [9, 45, 55, '99', '297', 703, 999, '2223', 2728, '4879']
test_2 = [10, 46, 56, 100, 298, 704, '1000', '2224', '2729', '4880']
test_3 = ['6', 'A', 'F', '33', '55', '5B', '78', '88', 'AB', 'CD', 'FF', '15F', '334', '38E']

print([kaprekar(i) for i in test_1]) # Тест чисел Капрекара из системы с основанием 10

print([kaprekar(i) for i in test_2 ]) # Тест НЕ чисел Капрекара из системы с основанием 10

print([kaprekar(i, base=16) for i in test_3]) #Т