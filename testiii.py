n = input()
rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
konv_num = [rom_num[i] for i in n]
for i in range(len(konv_num) - 1):
    if konv_num[i] < konv_num[i + 1]:
        konv_num[i] = konv_num[i] * (-1)
print(sum(konv_num))
