# Regression
Using the least square method for multielement regression
最小二乘法求多元线性回归

1.1	理论
最小二乘法（又称最小平方法）是一种数学优化技术。它通过最小化误差的平方和寻找数据的最佳函数匹配。利用最小二乘法可以简便地求得未知的数据，并使得这些求得的数据与实际数据之间误差的平方和为最小。最小二乘法还可用于曲线拟合。其他一些优化问题也可通过最小化能量或最大化熵用最小二乘法来表达。

多重线性回归的模型假设
y_i=w*x_i+b
	对于拟合的效果，可以使用L2范数衡量：
f=Σ(y_i-(y_i ) ̂ )^2=(y_i-ax_i-b)^2
当f的值取得最小值时，此时的拟合效果最小，当然另X_n=1则将上式中的b可以改写成矩阵式，F=(Y-W*X)^2，展开如下：
(Y-W*X)^T*(Y-W*X)
(Y^T-X^T*W^T )*(Y-W*X)
Y^T*Y-2X^T*W^T*Y+X^T*W^T*W*X
对W求导并另导数为0，可以得到：
W=(X^T*X)^I*X^T*Y

第三章 实验
本实验分别以随机数据和经典数据集为例
3.1. 随机数实践
随机产生5个值作为方程的W，如图1-1然后随机产生一组40*5 的矩阵作为X，再产生40*1 的矩阵作为 noise ，根据公式 ：
	Y=W*X+noise
与此同时，我们因为需要计算noise，因此我在每个X的最后一项均加入了一个固定的值1，再将noise作为W矩阵的一部分，也就是最后一项变为：
noise=noise*x_n，(x_n=1)，
因此我们的公式可以统一起来：Y=W*X，现在拿到了X和Y，如图1-2，我们再反过来通过最小二乘法来拟合这个系数矩阵W即可。


最小二乘法多元在波士顿房价预测上的应用
3.2.1 波士顿房价预测数据集介绍
1. Title: Boston Housing Data

2. Sources:
   (a) Origin:  This dataset was taken from the StatLib library which is
                maintained at Carnegie Mellon University.
   (b) Creator:  Harrison, D. and Rubinfeld, D.L. 'Hedonic prices and the 
                 demand for clean air', J. Environ. Economics & Management,
                 vol.5, 81-102, 1978.
   (c) Date: July 7, 1993

3. Past Usage:
   -   Used in Belsley, Kuh & Welsch, 'Regression diagnostics ...', Wiley, 
       1980.   N.B. Various transformations are used in the table on
       pages 244-261.
    -  Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning.
       In Proceedings on the Tenth International Conference of Machine 
       Learning, 236-243, University of Massachusetts, Amherst. Morgan
       Kaufmann.

4. Relevant Information:

   Concerns housing values in suburbs of Boston.

5. Number of Instances: 506

6. Number of Attributes: 13 continuous attributes (including "class"
                         attribute "MEDV"), 1 binary-valued attribute.

7. Attribute Information:

    1. CRIM      per capita crime rate by town
    2. ZN        proportion of residential land zoned for lots over 
                 25,000 sq.ft.
    3. INDUS     proportion of non-retail business acres per town
    4. CHAS      Charles River dummy variable (= 1 if tract bounds 
                 river; 0 otherwise)
    5. NOX       nitric oxides concentration (parts per 10 million)
    6. RM        average number of rooms per dwelling
    7. AGE       proportion of owner-occupied units built prior to 1940
    8. DIS       weighted distances to five Boston employment centres
    9. RAD       index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks 
                 by town
    13. LSTAT    % lower status of the population
14. MEDV     Median value of owner-occupied homes in $1000's

3.2.2 数据集预处理及思路
数据集部分截图如图1-4
 
图1-4 波士顿房价数据集（部分）

最后一项即是Y，前面的部分即是X，将本数据提取出来，按照合适的比例划分训练集和测试集，使用训练集调用之前写的代码预测出回归方程，并将测试集数据代入测试，并与真实的Y值进行对比，计算误差。
在实际预处理中，发现该数据集以空格分割，因此需要利用空格来分割，并且将得到的每个数字字符串转化为数字。如图1-5

 
图1-5
最终得到的X和Y 如图 1-6
 
图1-6

3.2.3 计算
将前400行数据传入之前定义的代码，得到回归方程如下，图1-7

 
图1-7 最小二乘法得到的回归方程

3.2.4 评估
将后面的数据代入图1-7 所示的回归方程，会得到一个新的向量 Y_new 将其与数据集中的真实值进行比较，算出误差，算误差的思路是使用两者差值的绝对值之和除以真实值的绝对值之和（即L1范数），就是：
evaluation=Σ(|（Y_(new,i)-Y_i ）|)/Σ(|Y_i |)
最后得到的准确率是：
 
 
