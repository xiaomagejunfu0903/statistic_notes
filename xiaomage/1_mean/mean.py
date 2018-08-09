#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: mean.py
#Brief: 使用python 求mean
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-03 22:00:53
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/xiaomagejunfu0903/statistic_notes
#############################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode


num_begin = 1
num_end = 11
cnt = 5
#1.取1-10之前的4个随机数
sample_nums = np.random.randint(num_begin,num_end,cnt)
print("random ints:{}".format(sample_nums))

#求算术平均值
mean = np.mean(sample_nums)
print("mean:{}".format(mean))

#求中位数
median = np.median(sample_nums)
print("median:{}".format(median))

#求众数
counts = np.bincount(sample_nums)
print("counts:{}".format(counts))
mode1 = np.argmax(counts)
print("mode1:{}".format(mode1))

mode2,m2_cnt = mode(sample_nums)
print("mode2:{}, count:{}".format(mode2, m2_cnt))

#画一组随机数的散点图
y = [0,0,0,0,0]
plt.scatter(sample_nums,y,c='r',s=25,alpha=0.4,marker='o')
plt.plot(mean, 0, 'bo')
plt.plot(median, 0, 'g*')
plt.plot(mode2, 0, 'k+')
plt.show()


