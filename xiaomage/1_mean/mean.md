# 期望

## 前导

假设,盒子里面有n个球，每个球贴上了一个标签，标签上的数字是1-8；那么，从盒子中任取10个球，每次取球的过程相互独立。

1,2,3,4,5,5,7,7,7,8-总共10个数

$$\displaystyle \begin{array}{rcl}  mean &=& \frac {1+2+3+4+5+5+7+7+7+8}{10} \\ &=& \frac{1*1+1*2+1*3+1*4+2*5+3*7+1*8}{10} \\ &=& \frac{1}{10}*1 +\frac{1}{10}*2+\frac{1}{10}*3 + \frac{1}{10}*4+\frac{2}{10}*5+\frac{3}{10}*7+\frac{1}{10}*8 \\ &=& P(X=1)*1 + P(X=2)*2+P(X=3)*3+P(X=4)*4+P(X=5)*5+P(X=7)*7+P(X=8)*8\end{array}$$

按照如上的推算过程，直观上演示了 算术平均值 到 数学期望的 演变过程。

所以，算术平均值 和 数学期望 本是同根生。

## 定义

[definition of mean from wiki:](https://en.wikipedia.org/wiki/Mean)

> In mathematics, mean has several different definitions depending on the context.
>
> In probability and statistics, **population mean** and **expected value** are used synonymously to refer to one measure of the central tendency either of a probability distribution or of the random variable characterized by that distribution.In the case of a discrete probability distribution of a random variable X, the mean is equal to the sum over every possible value weighted by the probability of that value; that is, it is computed by taking the product of each possible value x of X and its probability p(x), and then adding all these products together, giving $\displaystyle \mu =\sum xp(x)$. An analogous formula applies to the case of a continuous probability distribution. Not every probability distribution has a defined mean; see the Cauchy distribution for an example. Moreover, for some distributions the mean is infinite.
>
> For a data set, the term **arithmetic mean**, **mathematical expectation**, and sometimes **average** are used synonymously to refer to a central value of a discrete set of numbers: specifically, the sum of the values divided by the number of values. The arithmetic mean of a set of numbers x1, x2, ..., xn is typically denoted by $\displaystyle {\bar {x}}$ , pronounced "x bar". If the data set were based on a series of observations obtained by sampling from a statistical population, the arithmetic mean is termed the sample mean (denoted $\displaystyle {\bar {x}}$) to distinguish it from the population mean (denoted $\displaystyle \mu $ or $\displaystyle \mu _{x}$).

在概率论和统计学中，期望的定义: 随机变量X与其概率的加权和。也即，每个随机变量x的值乘以P(x)，然后再把所有的乘积项相加。是最基本的数学特征之一，是基石，是衡量随机变量分布的集中趋势，完全理解期望非常重要。

## 表示符号

$\mu$

$\displaystyle E[X]$

## 公式

对于离散型随机变量,期望的公式:$\mu=\sum xP(x)$

对于连续性随机变量,期望的公式:$\mu = \int_{-{\infty}}^{\infty} xf(x)dx$

