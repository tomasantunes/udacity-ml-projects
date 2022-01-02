#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import joblib
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = joblib.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

pois_count = 0

for i in pred:
    if i == 1:
        pois_count += 1

print("The number of POIs is: " + str(pois_count))
print("The number of people is: " + str(len(pred)))

true_positives_count = 0
for i in range(len(pred)):
    if pred[i] == 1 and labels_test[i] == 1:
        true_positives_count += 1

print("The number of true positives is: " + str(true_positives_count))

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

acc = accuracy_score(pred, labels_test)
precision = precision_score(pred, labels_test)
recall = recall_score(pred, labels_test)
print("Accuracy is: " + str(acc))
print("Precision is: " + str(precision))
print("Recall is: " + str(recall))
