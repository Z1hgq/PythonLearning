# -*- coding: utf-8 -*-
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing

#data = datasets.load_breast_cancer() #加载数据集

file_path = 'transfusion.data'
tmp = np.loadtxt(file_path, dtype=np.str, delimiter=",")
data_X = tmp[:,0:4].astype(np.float)#加载数据部分
data_y = tmp[::,-1].astype(np.float)#加载类别标签部分
# data_X = data.data
# data_y = data.target
# print(data)
#data normalization
data_X = preprocessing.scale(data_X)

#划分训练数据集和测试数据集，测试数据集占数据集的0.2
X_train,X_test,y_train,y_test = train_test_split(data_X,data_y,test_size = 0.2)

knn = KNeighborsClassifier()
#进行训练
knn.fit(X_train,y_train)
# #正确率
# print(knn.score(X_test,y_test))
#预测值
print('transfusion:')
print('预测值:',knn.predict(X_test))
#实际值
print('实际值:',y_test)
#十折交叉验证
scores = cross_val_score(knn,data_X,data_y,cv=10,scoring='f1_micro')
print('F1指标正确率:',scores)
#平均正确率
print('F1指标平均正确率:',scores.mean())
