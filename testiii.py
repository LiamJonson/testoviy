import xlrd

rb = xlrd.open_workbook('trekking2.xlsx')
sheet = rb.sheet_by_index(1)
sheet1 = rb.sheet_by_index(0)

vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
vals1 = [sheet1.row_values(rownum) for rownum in range(sheet1.nrows)]
kall = 0
gProt = 0
gFats = 0
gCarb = 0
k = []
for i in vals1[1:]:
    for j in vals[1:]:
        if i[0] == j[0]:
            k.append(i)
            k[-1].append(j[1])
for i in k:

    kall += float(i[1]) / 100 * float(i[5])
    gProt += float(i[2]) / 100 * float(i[5])
    gFats += float(i[3]) / 100 * float(i[5])
    if type(i[4]) == str:
        gCarb += 0
    else:
        gCarb += float(i[4]) / 100 * float(i[5])
print(int(kall), int(gProt), int(gFats), int(gCarb))


