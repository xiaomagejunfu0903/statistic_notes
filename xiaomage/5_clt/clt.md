# Central limit theorem(中心极限定理)

the **central limit theorem (CLT)** establishes that, in some situations, when independent random variables are added, their properly normalized sum tends toward a normal distribution (informally a "bell curve") even if the original variables themselves are not normally distributed.The theorem is a key concept in probability theory because it implies that probabilistic and statistical methods that work for normal distributions can be applicable to many problems involving other types of distributions.

当样本容量N趋于无穷大时，N个样本的均值的频率将 趋向于 正态分布。As your sample size become larger, the sampling distribution of the sampling mean will be close to a normal distribution.

在[大数定理](http://www.cnblogs.com/black-mamba/p/9440164.html)一节中，图 Figure2 很好的说明了 随着样本容量N的增大，样本均值的频率 趋向于 正态分布。

这里有个容易混淆的概念, 一般我们说一个样本就是指一次trial，而这里将 “一个样本”看作是 "容量为n的样本 整体作为一个样本"，然后 “一个样本”的样本均值的频率 趋向于 正态分布。

这两个定理都是 对 样本均值 的性质的描述,大数定理是说样本均值与总体均值的关系;中心极限定理是说样本均值的分布。利用大数定理我们可以用样本均值估计总体均值，利用中心极限定理 可以将较大容量的样本分布看做是正态分布。

## 示例

假设邮科院的工科男们有一个传统的活动，每学期组织一场与华师的联谊活动(你懂的！)，根据以往的经验，每个学生一天要喝2L水(标准差为0.7L)。这个学期呢，由于学校经费原因(是真穷哈！)，只能选50人参加该活动并带上110L水。那么，当天110L水被喝完的概率是多少?

从以上描述，可知，总体均值$\mu=2L$，总体标准差$\sigma=0.7L$；样本容量$n=50$，样本均值$\mu_{\overline x} \approx \mu = 2L$，样本方差$\sigma_{\overline x}^2$未知；由于样本容量为50时，那么，根据CLT，可以将样本分布看作是正态分布；这里，我们需要知道 P(110L水被喝完)。

"一个样本" $\overline x = \frac {110}{50}=2.2 L$，P(110L水被喝完)=P($\overline x > 2.2L$)

因为样本服从正态分布，我们可以用[z-table](http://www.cnblogs.com/black-mamba/p/9435988.html)去估算 概率。

$\sigma_{\overline x} = \frac {\sigma}{\sqrt n}=\frac {0.7}{\sqrt 50}=0.0989$(标准误差)

$z_{\overline x}=\frac{\overline x-\mu_{\overline x}}{\sigma_{\overline x}}=\frac {2.2-2}{0.0989}=2.022$

$P(\overline x > 2.2)=P(\frac {\overline x-\mu_{\overline x}}{\sigma_{\overline x}} > \frac{2.2-\mu_{\overline x}}{\sigma_{\overline x}})=P(z>2.022)=1-P(z<2.022)=1-0.97831=0.0217$,所以P(110L水被喝完)=0.0217.


![z-score](https://images2018.cnblogs.com/blog/593387/201808/593387-20180809092010452-391522075.png)