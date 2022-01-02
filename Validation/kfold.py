from sklearn.cross_validation import KFold

features, labels = getData()

kf = KFold(len(labels), 2)

for train_indices, test_indices in kf:
    features_train = [features[ii] for ii in train_indices]
    features_test = [features[ii] for ii in test_indices]
    labels_train = [labels[ii] for ii in train_indices]
    labels_test = [labels[ii] for ii in test_indices]



