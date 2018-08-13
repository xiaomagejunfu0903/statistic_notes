#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: ci_ex2.py
#Brief: 演示示例2
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-13 20:14:44
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/xiaomagejunfu0903/statistic_notes
#############################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats

#设置中文字体
zhfont = mpl.font_manager.FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc')

#95%置信水平的标准正态分布的置信区间演示
norm = scipy.stats.norm()
#x轴
x = np.linspace(norm.ppf(0.001),norm.ppf(0.999), 10000)
#y轴
y= norm.pdf(x)
#显示标准正态分布曲线
plt.plot(x,y)

#画置信区间的界限
plt.vlines(-1.96,ymin=0,ymax=norm.pdf(-1.96),colors='r', linestyles='dashed')
plt.vlines(1.96,ymin=0,ymax=norm.pdf(1.96),colors='r', linestyles='dashed')

#显示 置信区间
fill_x = np.linspace(-1.96,1.96,100)
#print("type of fill_x:{}".format(type(fill_x)))
fill_y = norm.pdf(fill_x)
#print("type of fill_y:{}".format(type(fill_y)))
plt.fill_between(fill_x, fill_y, color='b',alpha=0.5)

#已知置信水平，求置信区间

#方法1:不太准确
confidence = 95
c_low = (100-confidence)/2
c_high = 100-c_low
c_interval = np.percentile(x,[c_low, c_high])
print(c_interval)
plt.vlines(c_interval[0] ,ymin=0,ymax=0.3,colors='purple', linestyles='dashed')
plt.vlines(c_interval[1] ,ymin=0,ymax=0.3,colors='purple', linestyles='dashed')

#方法2:更好的方式
c_interval = [norm.isf(1-0.025),norm.isf(1-0.975)]
print(c_interval)
plt.vlines(c_interval[0] ,ymin=0,ymax=norm.pdf(-1.96),colors='r', linestyles='dashed',alpha=0.5)
plt.vlines(c_interval[1] ,ymin=0,ymax=norm.pdf(1.96),colors='r', linestyles='dashed',alpha=0.5)

plt.title('标准正态分布的95%置信区间',fontproperties=zhfont)
plt.savefig("ci_ex2.jpg")
#print("pdf(1.96):{}".format(norm.pdf(1.96)))
#print("cdf(1.96):{}".format(norm.cdf(1.96)))
#print("sf(1.96):{}".format(norm.sf(1.96)))
#print("isf(0.025):{}".format(norm.isf(0.025)))
plt.show()

