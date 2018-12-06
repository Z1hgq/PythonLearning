from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train,y_train)
# print(knn.score(X_test,y_test))
#
# from sklearn.model_selection import cross_val_score
# knn = KNeighborsClassifier(n_neighbors=5)
# scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
# print(scores.mean())

# X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)

# bayes = GaussianNB()
# bayes.fit(X_train,y_train)
# print(bayes.score(X_test,y_test))

designTree = tree.DecisionTreeClassifier()
designTree.fit(X_train,y_train)
print(designTree.score(X_test,y_test))
