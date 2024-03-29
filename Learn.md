# 机器学习
## 机械学习、示教学习、类比学习、归纳学习
- 机械学习(死记硬背型)、搜索
- 示教学习、类比学习 通过观察和发现学习
- 归纳学习 从样例中学习
### 从样例中学习
- 决策树和基于逻辑的学习
- 神经网络的连接主义学习
- 统计学习
## 算法类别
- 理解算法使用算法
- 不包括视觉领域、推荐系统、自然语言处理、时间序列分类
- 人工智能-机器学习-深度学习
- 带入问题学习知识
- - 如何评价算法的好坏
- - 如果解决过拟合和欠拟合
- - 如何调节算法的参数
- - 如何验证算法的正确性
### 分类任务(监督学习)
- 多分类
- - 图像识别
- - 数字识别
- - 一些算法只支持完成二分类的任务
- - 但是多分类的任务可以转化成二分类的任务
- - 多标签分类
### 回归任务(监督学习)
- - 结果是一个连续的数字的值,而非一个类别
### 批量学习和在线学习
- 批量学习 收集大量的数据（训练集） 构建模型（不会变化了） 新的数据输出使用
- - 优点 简单 适应环境变化（定时批量批量学习）缺点 数量大时间久 时间不等人
- 在线学习 收集大量的数据（训练集） 构建模型（会变化了） 新的数据输出使用
- - 优点 及时反应新的环境变化 缺点 不好的数据会带来不对的结果 需要加强对数据进行监控
### 参数学习和非参数学习
- f(x) = ax+b  --->为了学习到a和b值 不需要原有的
- 非参数 不对模型进行欧多的假设 非参数不等于没有参数
### 监督学习和非监督学习和半监督学习和增加学习
#### 监督学习（分类和回归）
给机器的训练数据标记和答案叫做监督学习，有x和y 称为监督学习
#### 非监督学习
    给机器没有任何答案和标记，对没有标记的数据进行分类-聚类分类
意义：对数据进行降维处理 特征提取：信用卡的信用评级和人的胖瘦无关 特征压缩：pca 方便可视化
异常检测
#### 半监督学习
一部分有标记和答案，另一部分没有
通常都先使用无监督学习手段对数据进行处理，之后使用监督学习手段做模型和预测
#### 增强学习
根据周围环境的情况，采取行动，根据采取行动的结果，学习行动方式
#### 数据即算法
数据确实非常重要
数据驱动
收集更多的数据
提高数据质量
提高数据的代表性
### numpy
- np.zeros(10)
- np.zeros(shape=(3,5),dtype=int)
- np.ones(10) 十个1
- np.full(shape=(3,5),fill_value=666) 3行5列的666
- np.arange(0,20,2)
- np.linspace(0,20,10) 从0到20 截除10个数 前壁后壁 都包含0，20
- np.random.randint(0,10)
- np.random.randint(0,10,size=[3,5]) 前壁后开的 有10个元素
- np.random.seed(666) 随机种子可以让每次随机出来的数值是一样的
- np.random.normal(10,100) 符合正态分布的随机浮点数
- np.random? 可以直接查文档
- np数组.reshape(2,5) 改变数组的为矩阵
-- 合并操作 
  - np.concatenate([x,y]) 两个np向量合并为一个向量
  - np.concatenate([A,A],axis=1) 沿着列的方向合并拼接
  - np.vstack([A,z]) 增加为行
  - np.hstack([A,B]) 增加为列
    
-- 分隔操作
    - x1,x2 = np.split(x,[5]) 分割0到5 和 分割 5之后
    - x1,x2 = np.split(x,[5],axis=1) 矩阵可以按照列进行分割
    - x1,x2 = np.vsplit
    - x1,x2 = np.hsplit
-- np的运算（universal functions）
    - 可以对np的数组直接进行加减乘除
    - np.linalg.inv(A) 为A的逆矩阵
    - np.linalg.pinv(A) 可计算出非正方矩阵的逆矩阵（违逆矩阵）
-- 聚合操作
    - np.sum 或者向量.sum np.sum(X,axis=0) 求列和
    - np.min np.argmin 最小值的索引位置
    - np.max
    - np.median() 中位数
    - np.mean() 均值
    - np.std() 标准差
    - np.partition(x,3) 找出比3小的数据在左边 比3大的数据在右边
-- fancy indexing
    - np数组的比较 x<3 获取一个布尔数组的返回
    - np.any 只要数组中有一个符合就返回true
    - np.all 所有的都要满足
### matplotlib
    - import matplotlib.pyplot as plt
    - plt.plot(x,y,color='red,linestyle='',xlabel,ylabel)
    - plt.axis([x,x1,y,y1]) 调整x,y的范围 
    - plt.xlabel("") 给x轴命名作用 
    - plt.ylabel("") 写y轴命名命名
    - plt.title() 添加标题
    - plt.show()
    - plt.scatter(x,y) 绘制散点图
### 加载数据(sklean里的数据集合)
### KNN
- 两个样本最相近的是哪个类别
- k近邻算法是非常特殊的，可以被认为是没有模型的算法
- 围栏和其他算法统一，可以认为训练数据集就是模型本身
- from sklean.neighbors import KNeighborsClassfier
- from sklearn.linear_model import SGDRegressor
- from sklean.metrics import accuracy_score
#### 超参数
- 概念：在算法运行前需要决定的参数 
- 模型参数： 算法过程中学习的参数
- knn算法没有模型参数
- knn算法中的k是典型的超参数
- 考虑距离的话 模不一样(距离的倒数 红色：1 蓝色 :1/3+1/4 = 7/12 红色胜)
- 距离的定义
- - 欧拉距离
- - 曼哈顿距离
- - 明可夫斯基距离 可以获得一个超参数P
- - 向量空间余弦相似度
- - 调整余弦相似度
- - 皮尔森相关系数
- - jaccard相似系数
##### 寻找好的超参数
- 领域知识
- 经验数值
- 实验搜索 如果寻找到的值是在我们定义范围内的边界的话 需要重新搜索
###### 网格搜索最佳超参数（Grid search）
param_grid = [
    {
        'weights':['uniform'],
        'n_neighbors':[i for i in range(1,11)]
    },
    {
        'weights':['distance'],
        'n_neighbors':[i for i in range(1,11)],
        'p':[i for i in range(1,6)],
    }
]
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(算法,param_grid,n_jobs) n_jobs 计算机多核处理 -1 自动取计算有几核 verbose
grid_search.fit(x,y) 比较慢
grid_search.best_estimator_ 返回最好的分类器
grid_search.best_score_ 最好的分数
grid_search.best_params_ 最好的参数
##### 数据归一化
- 解决方案：将所有的数据映射到同一尺度
- 最值归一化：把所有数据映射到0-1之间
- 使用Xcale 适用于分布有明显边界的情况下，受outlier影响较大 分数分值 和 图像像素的情况下
- 均值方差归一化(改进方案) standerdization 把所有数据归一到均值为0方差为1的分布中 适用于（数据分布没有明显的边界；有可能存在极端数据值） 
    （每个特征值 - 每个特征值的均值）/对应特征值的方
  from sklearn.preprocessing import StandardScalar
  standardScalar = StandardScalar()
##### k近邻算法缺点
- 效率低下
- 如果训练集有m个样本，n个特征 则预测每一个新的数据，需要O(M*N) 
- 高度数据相关
- 预测结果不具有可解释性
- 维数灾难 多维特征不适合 多维情况下可以降维
### 线性回归
- 通过分析问题,确定问题的损失函数或者效用函数;通过最优化损失函数或者效用函数，获得机器学习的模型
- 可以使用最优化原理和凸优化原理（需要自己学习）
- J(a,b)代表损失函数，求一个一次方程的最小值 就是对方程求导=0
#### 回归算法的评价
- 均方误差MSE
- 均方根误差RMSE 就是MSE开根号
- 平均绝对误差MAE
  - from sklearn.metrics import mean_squared_error 使用方法 mean_squared_error(y_test,y_predict)
  - from sklearn.metrics import mean_absolute_error  mean_absolute_error(y_test,y_predict)
- R squared(sklearn 内置的 评价方法)
- - R**2 <=1
    - R**2 = 1 - 使用我们的模型预测产生的错误/使用均值产生的错误（baseline Model）
- - 越大越好。当我们的预测模型不犯任何错误事，r方得到的最大值1
- - 当我们的模型等于基准模型时,r方为0
- - 如果r方<0，说明我们学习到的模型还不如基准模型。此时，很有可能我们的数据不存在任何性关系
### 多项式回归
- 增加特征值的操作
- 求解多元0 是指的多元线性回归的正规方程解 -> 时间复杂度高 是O(N^3)
- 多项式回归不需要对数据进行归一化处理 
  - from sklearn.linear_model import LinearRegression
- 识别欠拟合和过拟合（泛化能力）
- - 使用测试和训练数据集
- 学习曲线
- - 随着样本的增多，算法训练出的模型的表现力
- 解决测试数据集过拟合现象
- - 训练数据集 验证数据集（评判，调整超参数使用的数据集） 测试数据集
- - 交叉验证(k-folds) 留一法(LOO-CV)
### 梯度下降
- 使用梯度下降法 不一定是之前的目标函数 有可能会变
- 不是一个机器学习算法
- 是一种基于搜索的最优化方法
- 作用：最小化一个损失函数
- 梯度上升法：最大化一个效用函数
- n 称为学习率
- n的取值影响获取最优解的速度
- n的取值不合适，甚至得不到最优解
- n是梯度下降法的一个超参数
- - 优势
- scikit-learn中的SGD(随机梯度下降法)
from sklearn.linear_model import SGDRegressor
- 梯度的调试  
### 模型正则化
### PCA（降维）
- 一个非监督的机器算法
- 主要用于数据的降维
- 通过降维，可以发现更便于人类理解的特征
- 其他应用：可视化；去噪
from sklearn.decomposition import PCA
pca  = PCA(n_components=1)
pca.fit(x)
pca.transform(x)
  
### 多项式回归
- 为原来的样本数据增加了新的样本列
- 基于线性回归的算法 解决非线性问题 
- from sklearn.preprocessing import PolynomialFeatures
- poly = PolynomialFeatures(degree=2) 添加多少次的样本
- poly.fit(x)
- poly.transform(x)
### PolynomialFeatures
- 注意 如果有x1、x2特征 那么就会有1,x1,x2,x1^2 x1*x2 x2^2 六列特征
### Pipeline
from sklearn.pipline import Pipeline
from sklearn.preprocessing import StandardScaler

poly_reg = Pipline([
    ('poly', PolynomialFeatures(degree=2)),
    ('std_scaler',StandardScaler()),
    ('lin_reg',LinearRegression())
])
### 交叉验证
from sklearn.model_selection import cross_val_score
把训练集分成K份 称为 k-folds cross validation
### 模型误差
- 偏差+方差+不可避免的误差 = 模型误差
- 导致偏差的主要原因：对问题的本身的假设不正确！如：非线性数据使用线性回归
- 数据的一点点扰动都会较大的印象模型，通常原因使用的模型太过复杂，如高阶多项式回归
#### 偏差和方差
- 有一些算法天生是高方差的算法。如knn
- 非参数学习通常都是高方差算法。因为不对数据进行假设
- 有一些算法天生是高偏差算法，如线性回归
- 参数学习通常都是高偏差算法，因为数据具有极强的假设
##### 方差
- 机器学习的主要挑战，来自于方差
- 解决方差的通常手段
- - 降低模型复杂度
- - 减少数据维度；降噪
- - 增加样本数
- - 使用验证集
- - 模型正则化
####岭回归(模型正则化)
####LASSO Regression(可以用特征选择用)
- LASSO趋向于使得一部分theta值变为0.所以可作为特征选择用
#### 弹性网
L1正则项->LASSO
Ridge正则项->岭回归 L2正则项
### 逻辑回归
- 解决分类问题
- 通过预测的概率值来判断是否符合分类
- 逻辑回归即可以看做是回归算法，也可以看做是分类算法，通常作为分类用法，只可以解决二分类问题
- Sigmoid函数
### 决策边界
- 不规则的决策边界的绘制方法
### 逻辑回归使用正则化
from sklearn.linear_model import LogisticRegression
### OVR(ONE VS REST)  
from sklearn.multiclass import OneVsRestClassifier
### OVO(ONE VS ONE)
from sklearn.multiclass import OneVsOneClassifier
### 分类准确度的问题
- 对于极度偏斜的数据 只使用分类准确度是远远不够的
#### 混淆矩阵
- from sklearn.metrics import confusion_matrix
- 01的矩阵
- 精准率（precision= TP/TP+FP）做了多少次为1的且准确的 股票升跌
- - from sklearn.metrics import precision_score
- 召回率(recall= TP/TP+FN)真实的发生了预测发生了多少个 病人预测
- - from sklearn.metrics import recall_score
- F1 Score 两者都兼得 平常使
- pr曲线
- ROC曲线
- - FPR = FP/TN+FP  TPR = TP/FN+TP
### SVM(support vector machine)
- svm尝试寻找一个最优的决策边界，距离两个类别的最近的样本最远，这些样本就叫做支撑向量
- margin=2d svm要最大化margin,Hard Margin SVM,Soft Margin SVM
- 是一个有条件的最优化问题（hard Margin）
#### soft margin svm 和 svm的正则化
- 使用svm 要和knn一样 要对数据标准化处理 
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
#### 高斯核函数
- 将每一个样本点映射到一个无穷维的特征空间
#### 多项式特征
- 依靠升维使得原本线性不可分的数据线性可分
#### svm中使用多项式特征
###决策树
from sklearn.tree import DecisionTreeClassifier
max_depth=2,criterion="entropy"
- 非参数学习算法
- 可以解决分类问题
- 天然可以解决多分类问题
- 也可以解决回归问题
- 非常好的可解释性
- - 在那个维度做划分?维度在哪个值上做划分?怎么确定阈值
使用信息熵
#### 信息熵进行划分
- 随机变量不确定度的度量，熵越大，数据的不确定越高，熵越小，数据的不确定性越低
####基尼系数进行划分
- 值越大，数据的不确定越高，值越小，数据的不确定性越低
- 熵信息的计算比基尼系数稍慢
- sklearn中默认为基尼系数
#### CART
- 剪枝:降低复杂度，解决过拟合
- max_depth 决策深度
- min_samples_split 有多少个节点才划分两边的内容
- min_samples_leaf 对一个叶子节点来说至少有多少个样本呢
####决策树的局限性
- 对个别数特别敏感
### 集成学习
from sklearn.ensemble import VotingClassifier
voting_clf= VotingClassifier(estimators=[
    ('log_clf',LogisticRegression()),
    ('svc_clf',SVC()),
    ('dt_clf',DecisionTreeClassifier())
],voting='hard')
- 投票 少数服从多数
- voting classifier
- soft Voting 根据权值投票
- 每个模型只看样本呢的一部分 一共500 每个看100 子模型可以是同一个算法（子模型并不需要太高的准确率 >51%）
#### Bagging 和 Pasting
- 取样方式 放回取样 不放回取样
- oob 放回取样导致一部分样本很有可能没有取到
- 不适用测试数据集，而使用这部分没有被取到的样本做测试或者验证
- 对于特征进行随机取样
- 即针对样本，又针对特征进行随机取样
### 随机树林
- 决策树在节点划分上，在随机的特征子集寻找最优划分特征
### Ada Boosting
- from sklearn.ensemble import AdaBoostClassifier
### Gradient Boosting
- from sklearn.ensemble import GradientBoostingClassifier
- - 解决回归问题
    from sklearn.ensemble import GradientBoostingRegressor
### Stacking
### 模型选择
### 模型调整