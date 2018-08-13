# Confidence interval(置信区间)

**confidence interval (CI)** is a type of interval estimate, computed from the statistics of the observed data, that might contain the true value of an unknown population parameter. The interval has an associated **confidence level** that, loosely speaking, quantifies the level of confidence that the parameter lies in the interval. More strictly speaking, the confidence level represents the frequency (i.e. the proportion) of possible confidence intervals that contain the true value of the unknown population parameter. In other words, if confidence intervals are constructed using a given confidence level from an infinite number of independent sample statistics, the proportion of those intervals that contain the true value of the parameter will be equal to the confidence level.

置信区间是 由 样本统计量得到的 对总体参数的 区间估计。(P.S:第一次看到这句话的人，肯定要疯，因为不知所云,不要着急，本文保证你能理解这句话的含义。)

置信水平，真实的总体未知参数 落在 可能的置信区间的 概率。"可能的置信区间":这里面包含了误差界限(margin of error)

置信区间是一个范围，包含 未知总体参数值 的范围。是基于 有限样本 对 总体未知参数的 估计。

Confidence intervals consist of a range of potential values of the unknown *population parameter*. However, the interval computed from a particular sample does not necessarily include the true value of the parameter. Since the observed data are random samples from the true population, the confidence interval obtained from the data is also random.

The desired level of confidence is set by the researcher (not determined by data). Most commonly, the 95% confidence level is used. However, other confidence levels can be used, for example, 90% and 99%.

Factors affecting the width of the confidence interval include the size of the sample, the confidence level, and the variability in the sample. A larger sample will, all other things being equal, tend to produce a better estimate of the population parameter.

一般总体不可能被完全统计，只能采用随机抽样的方式来进行统计。In practice, however, we select one random sample and generate one confidence interval, which may or may not contain the true mean。实际上，我们只能进行随机抽样，然后计算出一个置信区间，但该置信区间不定包含 被估计参数的真值，因为抽样值是从随机获取，那么置信区间也是不确定。

通常，对于总体参数的估计，有两种类型:点估计(point estimate)和置信区间估计(CI estimate)。为方便表述，下面我以 对总体期望$\mu$的估计 为例进行说明。

置信区间估计的基于:

1. 点估计，例如，对样本均值进行估计;
2. 设置置信水平，通常为95%，当然你可以设置其他任何值0-100都可以;
3. 点估计的标准误差(the standard error of the point estimate) 或者 抽样的差异性(the sampling variability);



Strictly speaking a 95% confidence interval means that if we were to take 100 different samples and compute a 95% confidence interval for each sample, then approximately 95 of the 100 confidence intervals will contain the true mean value (μ). In practice, however, we select one random sample and generate one confidence interval, which may or may not contain the true mean. The observed interval may over- or underestimate μ. Consequently, the 95% CI is the likely range of the true, unknown parameter. The confidence interval does not reflect the variability in the unknown parameter. Rather, it reflects the amount of random error in the sample and provides a range of values that are likely to include the unknown parameter. Another way of thinking about a confidence interval is that it is the range of likely values of the parameter (defined as the point estimate + margin of error) with a specified level of confidence (which is similar to a probability).

Suppose we want to generate a 95% confidence interval estimate for an unknown population mean. This means that there is a 95% probability that the confidence interval will contain the true population mean. Thus, P( [sample mean] - margin of error < μ < [sample mean] + margin of error) = 0.95.

严格的来讲，95%的置信区间是 如果我们进行抽样，随机抽取100个不同的样本，然后为每个样本计算一个95%置信区间，那么，100个置信区间中大约有95个会包含实际的总体期望$\mu$。现实情况中，我们抽取一个随机样本并得到一个置信区间，不一定能包含真实的总体期望。因此，95%的置信区间是一个可能包含真实总体参数的范围。置信区间并不反映总体未知参数的差异性(variability)，它反映的是样本中随机误差，同时提供一个可能包含总体未知参数的可能范围。置信区间也可以看作是 指定置信水平的点估计+误差界限。

假设，我们要计算 对总体期望 95%的置信区间。即，有95%的可能性，置信区间包含真实的总体期望。P( [sample mean] - margin of error < μ < [sample mean] + margin of error) = 0.95.



## 示例1

今年，某果园的产量是200,000个苹果，从中随机抽取36个苹果，其平均重量是112g(标准差为40g)，求200,000个苹果的平均重量在100到124克范围的概率？

已知：

​	总体:200,000

​	样本容量n:36 g，样本均值:$\overline x=112$ g，样本标准差: $S=40$ g

未知：

​	总体均值：$\mu$，总体标准差：$\sigma$

求：

​	$$P(100 \le \mu \le 124)$$

如果反复以样本容量36进行抽样，然后求样本均值，绘制样本均值的频率图，根据CLT，那么样本均值的抽样分布是服从正态分布的。$\sigma_{\overline x} = \frac {\sigma}{\sqrt n} $

根据[小马哥课堂-统计学-大数定理](https://www.cnblogs.com/black-mamba/p/9440164.html)，$\mu_{\overline x} =  \mu$，$\mu_{\overline x}$：the  mean of the sampling distribution of the sampling mean

$$\begin{array}{rcl} P(100\le\mu \le 124) &=>& \\ P(100\le \mu_{\overline x} \le 124) &=>& \\ \end{array}$$

又因为 $z=\frac {x-\mu}{\sigma}$，$\overline x$服从正态分布，那么$\displaystyle z=\frac{\overline x-\mu_{\overline x}}{\sigma_{\overline x}},\mu_{\overline x}=\overline x+z\cdot\sigma_{\overline x}$

$$\displaystyle \begin{array}{rcl} P(100\le \mu_{\overline x} \le 124) &=>& \\ P(100\le \overline x+z\cdot\sigma_{\overline x}\le 124)&=>&整理得 \\ P(\frac{100-\overline x}{\sigma_{\overline x}} \le z \le \frac{124-\overline x}{\sigma_{\overline x}})\end{array}$$

根据[小马哥课堂-统计学-标准误差](https://www.cnblogs.com/black-mamba/p/9451708.html)一节可知，$\displaystyle \sigma_{\overline x}=\frac {\sigma}{\sqrt n} \approx \frac{S}{\sqrt n}=\frac {40}{6}=6.67$，$\sigma_{\overline x}$：the standard deviation of the sampling distribution of the sampling mean，(样本标准差(the standard deviation of the sample) 估计 总体标准差(the standard deviation of the population))

$$\displaystyle \begin{array}{rcl}  P(\frac{100-\overline x}{\sigma_{\overline x}} \le z \le \frac{124-\overline x}{\sigma_{\overline x}}) &=> & \\ P(\frac{100-112}{6.67} \le z \le \frac{124-112}{6.67}) &=>& \\ P(-1.8\le z\le 1.8)  & & (\overline x 落在 样本均值的抽样分布 的1.8个标准差之间的概率) \end{array}$$

根据[小马哥课堂-统计学-z分数](https://www.cnblogs.com/black-mamba/p/9435988.html)一节查z-table可知，$P(z \le 1.8)=0.9641$，

$$P(-1.8 \le z \le 1.8)=(P(z \le 1.8)-0.5)\cdot 2=0.4641\cdot 2=0.9282$$

所以 200,000个苹果的平均重量在100到124克范围的概率是92.82% .也可以说，92.82%的置信水平，苹果的real mean weight落在的置信区间[100,124]。

## 示例2

In practice, we often do not know the value of the population standard deviation (σ). However, if the sample size is large (n > 30), then the sample standard deviations can be used to estimate the population standard deviation. 

在现实环境中，我们很少能知道总体的方差。但是，如果抽样样本的容量n>30，那么可以用样本标准差(S)估计总体标准差($\sigma$)，同时，样本均值的分布服从正态分布，那么我们就可以用z-table去估算 置信区间或者执行水平。

已知，根据大数定理和中心极限定理，样本均值的分布服从 期望=$\mu_\overline{x} = \mu$，标准差=$\sigma_{\overline x}=\frac{\sigma}{\sqrt n}$的正态分布。根据z-table，标准正态分布满足$P(-1.96 \le z \le 1.96) = 0.95$，即，变量z有95%的可能性落在-1.96~1.96之间。那么，$z=\frac{\overline x-\mu_{\overline x}}{\sigma_{\overline x}}=\frac{\overline x-\mu}{\frac{\sigma}{\sqrt n}}$。

$$\begin{array}{rcl} P(-1.96 \le \frac{\overline x-\mu}{\frac{\sigma}{\sqrt n}} \le 1.96) &=&0.95 \\  P(\overline x-1.96\cdot\frac{\sigma}{\sqrt n} \le\mu \le \overline x+1.96\cdot\frac{\sigma}{\sqrt n})   &=& 0.95 \\\end{array}$$

那么，$\mu$所在的范围是$\overline x\pm1.96\cdot\frac{\sigma}{\sqrt n}$, 误差界限是$1.96\cdot\frac{\sigma}{\sqrt n}$。



## 置信区间与置信水平，样本容量的关系

1. 在置信水平固定的情况下，样本容量越大，置信区间越窄，抽样误差越小；
2. 在样本容量相同的情况下，置信水平越高，置信区间越宽；