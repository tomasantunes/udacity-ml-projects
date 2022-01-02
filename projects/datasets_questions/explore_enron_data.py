#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))

# print("The persons are: " + str(enron_data.keys()))

# print("The total data is: " + str(enron_data))

people_count = len(enron_data)

print("Nr of persons is: " + str(people_count))

print("Nr of features is: " + str(len(enron_data["PRENTICE JAMES"])))

pois = []
for i in enron_data:
    if (enron_data[i]['poi'] == 1):
        pois.append(enron_data[i])

pois_count = len(pois)

print("Nr of POIs is: " + str(pois_count))

print("James Prentice stock value is: " + str(enron_data['PRENTICE JAMES']['total_stock_value']))

print("Wesley Colwell nr of emails to POIs is: " + str(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))

print("Jeffrey K Skilling stock options value is: " + str(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))

print("Jeffrey K Skilling was paid: " + str(enron_data['SKILLING JEFFREY K']['total_payments']))

print("Kenneth Lay was paid: " + str(enron_data['LAY KENNETH L']['total_payments']))

print("Andrew Fastow was paid: " + str(enron_data['FASTOW ANDREW S']['total_payments']))

people_with_salary = 0
people_with_email = 0
people_without_payments = 0
pois_without_payments = 0

for i in enron_data.keys():
    person = enron_data[i]
    if person['salary'] != 'NaN':
        people_with_salary += 1
    if person['email_address'] != 'NaN':
        people_with_email += 1
    if person['total_payments'] == 'NaN':
        people_without_payments += 1
    if person['poi'] == 1 and person['total_payments'] == 'Nan':
        pois_without_payments += 1

print("The number of people with salary is: " + str(people_with_salary))

print("The number of people with an email address is: " + str(people_with_email))

print("The number of people without payments is: " + str(people_without_payments))

percentage_of_people_without_payments = people_without_payments / people_count * 100

print("The percentage of people without payments is: " + str(percentage_of_people_without_payments))

print("The number of POIs without payments is: " + str(pois_without_payments))

percentage_of_pois_without_payments = pois_without_payments / pois_count * 100

print("The percentage of POIs without payments is: " + str(percentage_of_pois_without_payments))

# If we add 10 people as POIs without payments

print("If we add 10 people the total number of people would be: " + str(people_count + 10) +  " and the number of people without payments would be: " + str(people_without_payments + 10))

print("If we add 10 POIs the total number of POIs would be: " + str(pois_count + 10) + " and the number of POIs without payments would be: " + str(pois_without_payments + 10))







