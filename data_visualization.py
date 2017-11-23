#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl

month_list = {}  # key: 月份，value: 本月微博条数
day_list = {}  # key: 天数， value: 当天微博条数
# 开始计算数量
with open('tianyuax_weibo.txt', 'rb') as f:
    for line in f:
        month = line.decode('utf-8')[1:3]
        day = line.decode('utf-8')[1:6]
        if month not in month_list:
            month_list.setdefault(month, 1)
        else:
            month_list[month] += 1
        if day not in day_list:
            day_list.setdefault(day, 1)
        else:
            day_list[day] += 1

# 将微博数量按顺序保存为一个list
month_counts = []
for m in sorted(month_list.keys()):
    month_counts.append(month_list[m])
day_counts = []
for d in sorted(day_list.keys()):
    day_counts.append(day_list[d])

# 开始做第一个图
X_m = range(1, len(month_counts) + 1)
plt.figure(figsize=(8, 8))
plt.xlabel('Month')  # 横轴：月份
plt.ylabel('Weibo Amount')  # 纵轴：微博数量
plt.bar(X_m, month_counts, facecolor = 'lightskyblue')
for x,y in zip(X_m,month_counts):
    plt.text(x, y+0.05, '%d' % y, ha='center', va= 'bottom')
plt.xticks(X_m)
plt.savefig('amount_month.png')
plt.show()
plt.close()

# 开始做第二个图
X_d = range(1, len(day_counts) + 1)
plt.figure(figsize=(10, 5))
plt.xlabel('Day')  # 横轴：天数
plt.ylabel('Weibo Amount')  # 纵轴：微博数量
# plt.bar(X_d, day_counts, facecolor = 'lightskyblue')
pl.plot(X_d, day_counts, linewidth=0.5, color='red')
plt.savefig('amount_day.png')
plt.show()
plt.close()
