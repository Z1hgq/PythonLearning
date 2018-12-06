# -*- coding: utf-8 -*-
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

# data = datasets.load_breast_cancer() #加载数据集
# data_X = data.data
# data_y = data.target
file_path = 'transfusion.data'
tmp = np.loadtxt(file_path, dtype=np.str, delimiter=",")
data_X = tmp[:,0:4].astype(np.float)#加载数据部分
data_y = tmp[::,-1].astype(np.float)#加载类别标签部分

#划分训练数据集和测试数据集，测试数据集占数据集的0.2
X_train,X_test,y_train,y_test = train_test_split(data_X,data_y,test_size = 0.2)

bayes = GaussianNB()
#进行训练
bayes.fit(X_train,y_train)
#预测值
print('transfusion:')
print('预测值:',bayes.predict(X_test))
#实际值
print('实际值:',y_test)
#十折交叉验证
scores = cross_val_score(bayes,data_X,data_y,cv=10,scoring='f1_micro')
print('F1指标正确率:',scores)
#平均正确率
print('F1指标平均正确率:',scores.mean())
