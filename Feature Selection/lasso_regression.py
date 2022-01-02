from sklearn.linear_model import Lasso

features, labels = getData()
clf = Lasso()
clf.fit(features, labels)
print(clf.coef_)