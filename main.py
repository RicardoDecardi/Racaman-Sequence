import xlwt
import matplotlib.pyplot as plt

wb = xlwt.Workbook()
sheet1 = wb.add_sheet("Entries")

# index
x = 0
# step
n = 0
# occupied indices
occupied = []

p = 0


def check(index, step, occupied):
    down = index - step
    up = index + step

    if down > 0 and down not in occupied:
        return down
    else:
        return up


def loop(n, x, occupied, p):
    for that in range(x, x + 50000):
        n += 1
        x = check(x, n, occupied)
        occupied.append(x)
        sheet1.write(n, p, x)


for column in range(0, 2):
    loop(n, x, occupied, p)
    p += 1

print(occupied)
wb.save('test.xls')
