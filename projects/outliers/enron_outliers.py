#!/usr/bin/python3

import joblib
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]

data_dict.pop("TOTAL", 0 )

data = featureFormat(data_dict, features)


### your code below
salaries = []
bonuses = []
count = 0

for point in data:
    salary = point[0]
    bonus = point[1]
    salaries.append(salary)
    bonuses.append(bonus)
    matplotlib.pyplot.scatter( salary, bonus )
    count += 1

ind = salaries.index(max(salaries))

print(data[ind])

largest_salaries = sorted(salaries)[-4:]
largest_bonuses = sorted(bonuses)[-4:]

print(largest_salaries)
print(largest_bonuses)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
