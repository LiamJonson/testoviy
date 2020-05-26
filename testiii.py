import xlrd
import io
import zipfile
import requests
r = requests.get("https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip")
with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
    archive.extractall()
x = 1
xy = []
while x !=1001:
    rb = xlrd.open_workbook(str(x) + '.xlsx')
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    g = [vals[1][1], int(vals[1][3])]
    xy.append(g)
    #print(vals[1][1], int(vals[1][3]))
    x += 1
for i in sorted(xy):
    print(*i)






