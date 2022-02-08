# learning_journey

## 环境配置
#### jupyter 配置虚拟环境
1. 在主环境执行 conda install nb_conda  
2. 进入虚拟环境 conda activate py2  
3. 执行 conda install nb_conda  即可在jupyter上刷新出现要的kernel  
4. 退出虚拟环境 conda deactivate

#### Jupyter中删除虚拟环境步骤
1. 查看安装了哪些虚拟环境kernel（在base或虚拟环境下运行都可以）：jupyter kernelspec list
2. 删除指定的kernel：jupyter kernelspec uninstall myenv

#### 用复制的办法重命名conda虚拟环境
1. 复制一个 conda create -n conda-new --clone conda-old
2. 删除旧的 conda remove -n conda-old --all

#### github网站下载上传代码速度太慢  
```fatal: unable to access 'https://github.com/xxxx.git/': OpenSSL SSL_connect: Connection was reset in co nnection to github.com:443```
有可能是因为github的IP地址更新了，手动更新即可。
https://blog.csdn.net/z1026544682/article/details/86635367  

#### jupyter上matplotlib的使用(结合官方文档食用)
https://blog.csdn.net/weixin_42042680/article/details/80738699
https://matplotlib.org/

## 线性回归(Linear Regression)21.06.13    
`path: \linear_regression\linear_regression.ipynb`  
用均方误差(MSE)做Loss function，用定步长(学习率)的梯度下降法(Gradient descent)逼近线性函数。  

#### 总结
1. ##### 线性回归是回归。目的：由已知的特征推断出目标函数值。
   $h_\theta(x) = a \in \mathbb{K}$, 其中$\mathbb{K}$是一个数域。
2. ##### 线性回归的模型一般形式  
   对$x = (1, x_1, x_2, ...,x_n)^T\in\mathbb{K}^{n+1},$  
   $$h_\theta(x) = \theta^Tx = \theta_0 + \theta_1x_1+\theta_2x_2+...+\theta_nx_n.$$  
   其中$\theta = (\theta_0, \theta_1, \theta_2, ..., \theta_n)^T \in\mathbb{K}^{n+1}.$   
3. ##### 线性回归常用的损失函数(Loss Function)：（$m$是训练集中样本的总个数）
   $$J(\theta) = \frac{1}{m}\sum_{i=1}^m\frac{1}{2}Cost(\theta,x^i,y^i), \quad where\quad Cost(\theta,x^i,y^i) = (h_\theta(x^i)-y^i)^2.$$
   我们希望损失函数（或称为罚函数）尽可能的小，换言之，希望找到一个合适的$\theta$使得$J(\theta)$是最小的。
4. ##### 如何寻找这样的 $\theta$ ：梯度下降
   （略，其实准确的说应该负梯度下降法），这里就不具体地展开了，毕竟我是数学系的hhhhh。  
   $$\begin{cases}
   \theta := \theta -\alpha \frac{\partial J(\theta)}{\partial \theta}\\
   \frac{\partial J(\theta)}{\partial \theta} = \frac{1}{m}\sum_{i=1}^m(h_\theta(x^i)-y^i)x^i =  \frac{1}{m}\sum_{i=1}^m(\theta^Tx^i-y^i)x^i.
   \end{cases}$$
   其中$\alpha$ 为学习率。
5. ##### 特征缩放的原因
   1. 回归系数直接受特征范围的影响，特征范围大的一般系数会比放缩后的更夸张，例子：为了方便，我们假设$\theta_0 = 0$。对正规后的$x,y$, 分别取$x:y, 100x:100y$做线性回归，我们知道：$\theta_{100}=\theta_{norm}$，
       $\frac{\partial J_{norm}(\theta)}{\partial \theta} = \frac{1}{m}\sum_{i=1}^m(\theta^Tx^i-y^i)x^i.$，而  
       $\frac{\partial J_{100}(\theta)}{\partial \theta} = \frac{1}{m}\sum_{i=1}^m(100\theta^Tx^i-100y^i)100x^i = \frac{10^4}{m}\sum_{i=1}^m(\theta^Tx^i-y^i)x^i.$  
       ！！！这意味着什么！意味着对同一起点$\theta$，$100x:100y$给出的梯度是标准化后的10000倍！有很大的概率会跳过极小值点！在$J(\theta)$的函数图像上是“之”字形上升的。
   2. 具有较高比例的功能比具有较低比例的功能更重要；
   3. 如果我们具有缩放值，则可以轻松实现渐变下降；
   4. 如果按比例缩放，某些算法将减少执行时间；
   5. 一些算法基于欧几里得距离，欧几里得距离对特征尺度非常敏感。
   

#### 自问自答
1. Q: 如果数据总量过大（即$m$过大），那么对$J(\theta)$关于$\theta$求导时数据量过大，更新一次$\theta$计算量很大怎么办？而且要每段时间都训练一次么？那样本数的增加，计算难度很大。 
   A: 
   1. 这里牵扯到两个概念：**全量训练**和**增量训练**。顾名思义。  
   2. 我们可以把较大的样本集随机划分成若干小的子集，对每个小子集，我们分别对每个子集进行一次$\theta$值的更新，也许最后得到的$\theta$值不如直接对所有样本进行梯度下降的结果准确。  
   从概率的角度看，因为选择样本子集是独立等可能性的，所以我们的这部分子集的分布可以近似认为是全体样本的分布，因此最后的$\theta$仍然会是收敛的。(除非特别点背)  
   换言之，我们把全体数据，切分成了若干大小合适的子集$S_1,S_2,...$，并且在这些子集上服从的分布与全体数据服从的分布近似相同，那么在误差允许的范围内，$J(\theta)$在$S_{i+1}$上关于$\theta$的偏导也可以认为是$J(\theta)$在$S$上关于$\theta$的偏导。
2. Q: 如果特征范围区别较大，但又无法放缩怎么办？
   A: 在5.1的情形下，我尝试将**学习率**降低（/10)，使得我的linear regression重新收敛。也就是说，想办法平衡掉偏导过大。

## 逻辑回归(Logistic Regression)21.07.04  
   使用logistic(Sigmoid)函数复合在线性函数外。
   $$ 
   \begin{aligned}
      g(z)=&\frac{1}{1+e^{-z}}\\
   g(h_\theta(x))=&\frac{1}{1+e^{-\theta^{T}x}}
   \end{aligned}$$


#### 自问自答
1. 为什么要是用$Logistic$回归作分类？
用线性回归后指定阈值作分类，则线性回归极容易受到极端值的影响。用$logistic$函数嵌套会在相当程度上削弱极端值造成的影响。














