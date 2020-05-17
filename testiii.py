import xlrd

rb = xlrd.open_workbook('trekking1.xlsx')
sheet = rb.sheet_by_index(0)

vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
sub = vals[0][1]
result = {}
for i in vals[1:]:
    result[i[0]] = i[1]
k = sorted(result.items(), key=lambda x: (-x[1], x[0]))
for j,i in enumerate(k):
    print(i[0])
