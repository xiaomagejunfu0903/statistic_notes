#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: lln.py
#Brief: 以掷骰子为例，演示随着试验次数的增加，样本均值趋于总体均值
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-07 22:29:00
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/xiaomagejunfu0903/statistic_notes
#############################################
import numpy as np
import matplotlib.pyplot as plt

#总实验次数
total_num = 1000
#骰子的6面
num_sides = 6

plt.figure(1)

#设置x轴的范围
xmin, xmax = plt.xlim(0, total_num)
print("xmin:{},xmax:{}".format(xmin,xmax))

#设置y轴的范围
ymin, ymax = plt.ylim(1, 6)
print("ymin:{},ymax:{}".format(ymin,ymax))

#设置坐标轴的名称
plt.xlabel('number of trials')
plt.ylabel('average')



#画均值线
plt.plot((0,total_num),(3.5,3.5),c='b')

l = []
n_s = range(1, total_num)

#number of trials:n,mean of sample:average
for n in  n_s:
    average = np.mean(np.random.randint(1,7,n))
    l.append(average)
    #print("n:{},average:{}".format(n, average))
    #plt.scatter(n,average,c='r',s=1,alpha=0.5) 

plt.plot(n_s,l,alpha=0.5,c='red')


plt.figure(2)
#设置x轴的范围
ymin, ymax = plt.ylim(0, total_num)
print("ymin:{},ymax:{}".format(ymin,ymax))
#设置y轴的范围
xmin, xmax = plt.xlim(1, 6)
print("xmin:{},xmax:{}".format(xmin,xmax))

#设置坐标轴的名称
plt.xlabel('number of trials')
plt.ylabel('average')

plt.plot((3.5,3.5),(0,total_num),c='b')

#plt.plot(l,n_s,alpha=0.5,c='red')
for n in  n_s:
    average = np.mean(np.random.randint(1,7,n))
    l.append(average)
    #print("n:{},average:{}".format(n, average))
    plt.scatter(average,n,c='r',s=1,alpha=0.5) 

plt.show()
