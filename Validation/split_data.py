from sklearn import cross_validation

features, labels = getData()

x_train, x_test, y_train, y_test = cross_validation.train_test_split(features, labels, test_size=0.4, random_state=0)