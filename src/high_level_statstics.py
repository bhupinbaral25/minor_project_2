import numpy as np

def calculate_statstics(numpy_array):
    my_dict = {
        "mean" : np.mean(numpy_array, axis=0),
        "Standard Deviation" : np.std(numpy_array, axis=0),
        "min" : np.min(numpy_array, axis=0),
        "max" : np.max(numpy_array, axis=0),
        "25%" : np.percentile(numpy_array, 25, axis=0),
        "median" : np.percentile(numpy_array, 50, axis=0),
        "75%" : np.percentile(numpy_array, 25, axis=0)
    }
    return my_dict