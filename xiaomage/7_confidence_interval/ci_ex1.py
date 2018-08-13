#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: ci_ex1.py
#Brief: 示例1
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-13 19:33:11
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/xiaomagejunfu0903/statistic_notes
#############################################
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import random

#随机抽取36个苹果，计算200,000苹果的重量在100到124g范围的概率
def sampling_distribution(data,confidence=0.95,sampling_times=1,sampling_size=30):
    list_sampling_mean = []
    
    for i in np.arange(sampling_times):
        #samples = np.random.choice(data,sampling_size)#重复抽样
        samples = random.sample(list(data),sampling_size)#不重复抽样
        #print("samples:{}".format(samples))
        samples_mean = np.mean(samples)
        list_sampling_mean.append(samples_mean)
        
    
    #the sampling distribution of the sampling mean,样本均值的抽样分布
    sam_mean = np.mean(list_sampling_mean)
    print("样本均值分布的期望,sam_mean:{}".format(sam_mean))
    sam_std = np.std(list_sampling_mean)
    print("样本均值分布的标准差,sam_std:{}".format(sam_std))
    
    #获取样本均值分布~N(sam_mean, sam_std^2)
    norm = scipy.stats.norm(loc=sam_mean, scale=sam_std)
    
    #获取距离sam_mean 4个sam_std的范围
    x = np.arange(sam_mean-sam_std*4, sam_mean+sam_std*4, 1)
    #获取x对应的概率密度函数值
    y = norm.pdf(x)
    #显示样本均值分布
    plt.plot(x, y,'b--',alpha=0.7,label='sample distribution of the sample mean')

    #获取置信区间,方法1
    confidence *= 100
    c_low = (100 - confidence) / 2
    c_high = 100 - c_low
    c_interval = np.percentile(list_sampling_mean,[c_low, c_high])
    print("95%置信区间端点对应的x坐标:{}".format(c_interval))
    

    #获取置信区间,方法2
    c_interval1 = [norm.isf(1-0.025),norm.isf(1-0.975)]
    print("95%置信区间端点对应的x坐标:{}".format(c_interval1))
    print("[{},{}]".format(sam_mean-sam_std*1.8, sam_mean+sam_std*1.8))

    #绘制置信区间对应的竖线
    a = c_interval[0]
    b = c_interval[1]
    plt.vlines(a, 0, norm.pdf(a),'r')
    plt.vlines(b, 0, norm.pdf(b),'r')
    
    a1 = c_interval1[0]
    b1 = c_interval1[1]
    plt.vlines(a1, 0, norm.pdf(a1),'g',alpha=0.5)
    plt.vlines(b1, 0, norm.pdf(b1),'g',alpha=0.5)
    
    fill_x = np.linspace(a1,b1,100)
    #print("type of fill_x:{}".format(type(fill_x)))
    fill_y = norm.pdf(fill_x)
    #print("type of fill_y:{}".format(type(fill_y)))
    plt.fill_between(fill_x, fill_y, color='b',alpha=0.5)


#模拟总体200,000个苹果的重量数据
#用不同的数据测试
#data1 = np.random.randint(10, 200, size=200000)
data1 = np.random.randint(50, 200, size=200000)

#总体均值
population_mean = np.mean(data1)
print("population mean:{}".format(population_mean))

#总体标准差
population_std = np.std(data1)
print("population std:{}".format(population_std))

#总体分布曲线
norm1 = scipy.stats.norm(population_mean, population_std)
x = np.arange(population_mean-population_std*3.5, population_mean+population_std*3.5, 1)
y = norm1.pdf(x)
plt.plot(x, y,'r--',label='population distribution',alpha=0.7)


sampling_distribution(data1,sampling_times=1000,sampling_size=36) 
   
plt.legend()
plt.show() 
