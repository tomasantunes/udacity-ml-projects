def featureScaling(arr):
    xmin = min(arr)
    xmax = max(arr)
    
    if xmin != xmax:
        result = []
        for i in arr:
            x_rescaled = float(i - xmin) / float(xmax - xmin)
            result.append(x_rescaled)
        return result
    else:
        return [0.5] * len(arr)