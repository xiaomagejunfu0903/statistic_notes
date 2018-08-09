#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: variance.py
#Brief:
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-06 22:40:11
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/xiaomagejunfu0903/statistic_notes
#############################################
import numpy as np
import matplotlib.pyplot as plt

A = [2, 2, 3, 3]
B = [0, 0, 5, 5]

mean_A = np.mean(A)
print("mean_A:{}".format(mean_A))
mean_B = np.mean(B)
print("mean_B:{}".format(mean_B))

var_A = np.var(A)
print("var_A:{}".format(var_A))
var_B = np.var(B)
print("var_B:{}".format(var_B))

y_A = [0,0,0,0]
plt.scatter(A,y_A,c='r',s=25,marker='o')
plt.scatter(B,y_A,c='b',s=25,marker='*')
plt.plot(var_A, 2, 'k+')
#A_handle, = plt.plot((var_A,mean_A), (2,2))
plt.plot((var_B), (1), 'gD')
#A_handle, = plt.plot((var_B,mean_B), (1,1))

plt.plot((mean_A,mean_A),(0.0,2.5))#均值线

plt.plot((2,mean_A),(0.25,0.25),'peru')
plt.plot((3,mean_A),(0.50,0.50),'seagreen')

plt.plot((0,mean_B),(1.5,1.5),'magenta')
plt.plot((5,mean_B),(2.0,2.0),'hotpink')

plt.grid(True)
plt.show()
