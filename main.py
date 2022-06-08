import xlsxwriter
from math import *
import openpyxl
import numpy as np
import matplotlib.pyplot as plt


def mnk(first, second):
    x = sum(first)
    y = sum(second)
    x_kvad = []
    xy_un = []
    for i in first:
        x_kvad.append(i**2)
    for i in range(len(first)):
        xy_un.append(first[i]*second[i])
    xi = sum(x_kvad)
    xy = sum(xy_un)
    delta = xi * len(first) - x * x
    delta_a = xy * len(first) - x * y
    delta_b = xi * y - xy * x
    a = delta_a / delta
    b = delta_b / delta
    return a, b


def sglazh(n):
    values1 = []
    wb = openpyxl.load_workbook('data1.xlsx')
    sheet = wb['Sheet1']

    for j in range(1, n+1):
        value = sheet['%s%d' % ('A', j)].value
        values1.append(value)
    for i in range(len(values1)):
        if values1[i] is None:
            values1 = values1[0:i]
            break

    window = floor(len(values1)*0.25)
    if window < 1:
        window = 1
    values_sglazh = [values1[0]]
    n = 1
    summa = [values1[0]]
    while n < len(values1):
        if n % int(window) == 0:
            values_sglazh.append(sum(summa) / int(window))
            summa = [values1[n]]
            n += 1
        else:
            summa.append(values1[n])
            n += 1
    else:
        values_sglazh.append(sum(summa) / len(summa))

    print(values1)
    print(values_sglazh)

    a, b = mnk([i for i in range(len(values_sglazh))], values_sglazh)
    mnk_func = []
    for i in range(1, len(values_sglazh) + 1):
        mnk_func.append(a*i+b)
    print(a, b, mnk_func)

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    fig, ax = plt.subplots()
    ax.plot(mnk_func)
    ax.plot(values_sglazh)

    # Use automatic StrMethodFormatter
    ax.yaxis.set_major_formatter('{x:1.2f}')

    ax.yaxis.set_tick_params(which='major', labelcolor='green',
                             labelleft=False, labelright=True)

    plt.show()

    print('predicted value: ' + str(values1[-1]+(values1[-1]-values1[-2])))


def values(first, last, shag):
    result = []
    for x in range(first, last, shag):
        y = sin(x)+0.1*sin(x**5)
        result.append(y)
    return result


def writing():
    workbook = xlsxwriter.Workbook('data1.xlsx')
    worksheet = workbook.add_worksheet()
    first, last, shag = list(map(int, input().split()))
    result = values(first, last, shag)
    for i, x in enumerate(result):
        worksheet.write(i, 0, x)
    workbook.close()
    sglazh(last-first)


writing()