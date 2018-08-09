#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#############################################
#File Name: standard_error.py
#Brief:  直观上演示 标准误差公式 的正确性
#Author: frank
#Email: frank0903@aliyun.com
#Created Time:2018-08-09 20:29:10
#Blog: http://www.cnblogs.com/black-mamba
#Github: https://github.com/xiaomagejunfu0903 
#############################################
import random
import matplotlib.pyplot as plt
import numpy as np


n=10000

#list_population=list(np.random.normal(size=n))

list_population = list(np.random.randint(low=1,high=7,size=n))
#print("list_population:{},len:{}".format(list_population,len(list_population)))

#总体期望
mean_population=np.mean(list_population)
print("mean_population: %.6f"%mean_population)

#总体标准差
sigma=np.std(list_population,ddof=0)
print("standard deviation of population:{}".format(sigma))

#显示总体分布
plt.figure(1)
n,bins,patches = plt.hist(list_population,bins='auto',density=1)
y_population = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mean_population))**2))
plt.plot(bins, y_population, 'r--')
plt.title('population distribution')
text_comment = "$\mu={},\ \sigma={}$".format(mean_population,sigma)
plt.text(1, .5, text_comment,{'color':'r','fontsize':15})

#求单个样本估算的标准误
def get_sample_standard_error(sample):
    std=np.std(sample,ddof=0)
    standard_error=std/np.sqrt(len(sample))
    return standard_error

#抽样分布
#获取standard error of the mean
def get_SEM(list_population, simple_size, sampling_times):
    #进行 容量为simple_size的样本 抽样，抽样次数为sampling_times
    for i in range(sampling_times):
        samples=random.sample(list_population,simple_size)
        #print("samples:{}".format(samples))
        sampling_mean = np.mean(samples)
        #print("sampling mean:{}".format(sampling_mean))
        list_sampling_mean.append(sampling_mean)
    print("size of list_sampling_mean：{}".format(len(list_sampling_mean)))
    sampling_sd = np.std(list_sampling_mean,ddof=0)
    print("standard deviation of the sampling mean:{}".format(sampling_sd))
    return sampling_sd
    
#样本容量
simple_size = 10
#抽样次数
sampling_times = 1000
#样本均值list
list_sampling_mean = []

print("理论标准误:{}".format(sigma/np.sqrt(simple_size)))

sampling_sd = get_SEM(list_population, simple_size, sampling_times)
'''
#进行 容量为simple_size的样本 抽样，抽样次数为sampling_times
for i in range(sampling_times):
    samples=random.sample(list_population,simple_size)
    #print("samples:{}".format(samples))
    sampling_mean = np.mean(samples)
    #print("sampling mean:{}".format(sampling_mean))
    list_sampling_mean.append(sampling_mean)




print("size of list_sampling_mean：{}".format(len(list_sampling_mean)))
sampling_sd = np.std(list_sampling_mean,ddof=0)
print("standard deviation of the sampling mean:{}".format(sampling_sd))
'''
plt.figure(2)
n,bins,patches = plt.hist(list_sampling_mean,bins='auto',density=1)
y_population = ((1 / (np.sqrt(2 * np.pi) * sampling_sd)) * np.exp(-0.5 * (1 / sampling_sd * (bins - np.mean(list_sampling_mean)))**2))
plt.plot(bins, y_population, 'r--')
plt.title('sample distribution of the sample mean')
text_comment = "real $\mu={0:},\ \sigma={1:}$".format(np.mean(list_sampling_mean),sampling_sd)
plt.text(2.0, 0.4, text_comment,{'color':'r','fontsize':15})
text_comment = "theoretical standard error of the mean:{}".format(sigma/np.sqrt(simple_size))
plt.text(2.0, 0.8, text_comment,{'color':'m','fontsize':15})

plt.show()
