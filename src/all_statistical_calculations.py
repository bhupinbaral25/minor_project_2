import numpy as np


class StatisticalCalculations:
    def __init__(self, numpy_array, headers):
        self.numpy_array = numpy_array
        self.headers = headers
        self.axis = 0

    def get_mean(self):
        return np.round(np.mean(self.numpy_array, axis=self.axis))

    def get_min(self):
        return np.min(self.numpy_array, axis=self.axis)

    def get_max(self):
        return np.max(self.numpy_array, axis=self.axis)

    def get_std(self):
        return np.round(np.std(self.numpy_array, axis=self.axis))

    def get_first_quartile(self):
        return np.quantile(self.numpy_array, .25, axis=self.axis)

    def get_second_quartile(self):
        return np.quantile(self.numpy_array, .50, axis=self.axis)

    def get_third_quartile(self):
        return np.percentile(self.numpy_array, .75, axis=self.axis)

    def get_unique(self):
        return self.count_unique_duplicate()[0]

    def get_duplicate(self):
        return self.count_unique_duplicate()[1]

    def count_unique_duplicate(self):
        unique_list, duplicate_list = [], []
        for i in range(len(self.headers)-1):
            unique, count = np.unique(self.numpy_array[:, i], axis=self.axis, return_counts=True)
            unique_list.append(len(unique[count == 1]))
            duplicate_list.append(len(unique[count > 1]))
        return unique_list, duplicate_list
