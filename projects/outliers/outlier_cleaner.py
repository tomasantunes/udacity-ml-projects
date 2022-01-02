#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    points_to_remove = int(len(predictions) / 10)
    errors = []

    for i in range(len(predictions)):
        age = ages[i][0]
        net_worth = net_worths[i][0]
        prediction = predictions[i][0]
        error = abs(pow(net_worth - prediction, 2))
        errors.append(error)

    largest_errors = sorted(range(len(errors)), key = lambda sub: errors[sub])[-points_to_remove:]

    new_predictions = [element for i,element in enumerate(predictions) if i not in largest_errors]
    new_ages = [element for i,element in enumerate(ages) if i not in largest_errors]
    new_net_worths = [element for i,element in enumerate(net_worths) if i not in largest_errors]
    new_errors = [element for i,element in enumerate(errors) if i not in largest_errors]

    for i in range(len(new_predictions)):
        cleaned_data.append((new_ages[i], new_net_worths[i], new_errors[i]))
    
    return cleaned_data

