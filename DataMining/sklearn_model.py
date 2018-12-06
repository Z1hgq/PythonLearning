from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# X,y = datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=1)
#
# plt.scatter(X,y)
# plt.show()

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()

model.fit(data_X,data_y)

# print(model.predict(data_X[:4,:]))

# print(model.coef_)
# print(model.intercept_)
# print(model.get_params())
print(model.score(data_X,data_y)) #R^2 coeffcient of determination
