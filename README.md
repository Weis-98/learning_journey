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

## 21.06.13   
### 线性回归(Linear Regression)  
path: \linear_regression\linear_regression.ipynb  
用均方误差(MSE)做Loss function，用定步长(学习率)的梯度下降法(Gradient descent)逼近线性函数。  