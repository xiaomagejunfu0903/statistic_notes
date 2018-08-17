#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: t.py
#Brief:
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-17 23:07:24
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/xiaomagejunfu0903/statistic_notes
#############################################

from scipy.stats import t
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

df = 2
rv_t = t(df)
x = np.linspace(-4,4, 100)
plt.plot(x,rv_t.pdf(x),'y-',label='df=2')

x2 = np.linspace(-4,4, 100)
plt.plot(x2,t.pdf(x2,5),'g--',label='df=5')

x3 = np.linspace(-4,4, 100)
plt.plot(x3,t.pdf(x3,10),'b--',label='df=10')

x4 = np.linspace(-4,4, 100)
plt.plot(x4,t.pdf(x4,120),'r--',label='df=120')

x5 = np.linspace(-4,4, 100)
plt.plot(x5,norm.pdf(x5),'m--',label='std norm',alpha=0.5)

plt.legend()

plt.show()

