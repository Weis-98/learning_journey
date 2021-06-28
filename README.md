# learning_journey

## 21.06.12
### jupyter 配置虚拟环境
1. 在主环境执行 conda install nb_conda  
2. 进入虚拟环境 conda activate py2  
3. 执行 conda install nb_conda  即可在jupyter上刷新出现要的kernel  
4. 退出虚拟环境 conda deactivate

### Jupyter中删除虚拟环境步骤
1. 查看安装了哪些虚拟环境kernel（在base或虚拟环境下运行都可以）：jupyter kernelspec list
2. 删除指定的kernel：jupyter kernelspec uninstall myenv

### 用复制的办法重命名conda虚拟环境
1. 复制一个 conda create -n conda-new --clone conda-old
2. 删除旧的 conda remove -n conda-old --all

### github网站下载上传代码速度太慢  
```fatal: unable to access 'https://github.com/xxxx.git/': OpenSSL SSL_connect: Connection was reset in co nnection to github.com:443```
有可能是因为github的IP地址更新了，手动更新即可。
https://blog.csdn.net/z1026544682/article/details/86635367  

### jupyter上matplotlib的使用(结合官方文档食用)
https://blog.csdn.net/weixin_42042680/article/details/80738699
https://matplotlib.org/

## 21.06.13   
### 线性回归(Linear Regression)  
path: \linear_regression\linear_regression.ipynb  
用均方误差(MSE)做Loss function，用定步长(学习率)的梯度下降法(Gradient descent)逼近线性函数。  

#### 总结
1. 线性回归是回归。目的：由已知的特征推断出目标函数值。$h_\theta(x) = a \in \mathbb{K}$, 其中$\mathbb{K}$是一个数域。
2. 线性回归的模型一般形式是：  
   对$x = (1, x_1, x_2, ...,x_n)^T\in\mathbb{K}^{n+1},$  
   $$h_\theta(x) = \theta^Tx = \theta_0 + \theta_1x_1+\theta_2x_2+...+\theta_nx_n.$$  
   其中$\theta = (\theta_0, \theta_1, \theta_2, ..., \theta_n)^T \in\mathbb{K}^{n+1}.$   
3. 线性回归常用的损失函数(Loss Function)：（$m$是训练集中样本的总个数）
   $$J(\theta) = \frac{1}{m}\sum_{i=1}^m\frac{1}{2}Cost(\theta,x^i,y^i), \quad where\quad Cost(\theta,x^i,y^i) = (h_\theta(x^i)-y^i)^2.$$
   我们希望损失函数（或称为罚函数）尽可能的小，换言之，希望找到一个合适的$\theta$使得$J(\theta)$是最小的。
1.  如何寻找

#### 自问自答
1. Q: 如果数据总量过大（即$m$过大），那么对$J(\theta)$关于$\theta$求导时数据量过大，更新一次$\theta$计算量很大怎么办？而且要每段时间都训练一次么？那样本数的增加，计算难度很大。  
   A: 1.这里牵扯到两个概念：**全量训练**和**增量训练**。顾名思义。  
   2.我们可以把较大的样本集随机划分成若干小的子集，对每个小子集，我们分别对每个子集进行一次$\theta$值的更新，也许最后得到的$\theta$值不如直接对所有样本进行梯度下降的结果准确。  
   &emsp;&emsp;从概率的角度看，因为选择样本子集是独立等可能性的，所以我们的这部分子集的分布可以近似认为是全体样本的分布，因此最后的$\theta$仍然会是收敛的。(除非特别点背)  
   &emsp;&emsp;换言之，我们把全体数据，切分成了若干大小合适的子集$S_1,S_2,...$，并且在这些子集上服从的分布与全体数据服从的分布近似相同，那么在误差允许的范围内，$J(\theta)$在$S_{i+1}$上关于$\theta$的偏导也可以认为是$J(\theta)$在$S$上关于$\theta$的偏导。
2. 
