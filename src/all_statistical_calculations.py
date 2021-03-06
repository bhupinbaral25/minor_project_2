import numpy as np


class StatisticalCalculations:
    """
    :param numpy_array: numpy array of elements of csv
    :param headers: list of headers of csv
    :functions: All are high level statistical calculation,
                call using get_{func_name} eg. get_mean()
    """
    def __init__(self, numpy_array, headers):
        self.data_array = numpy_array
        self.headers = headers
        self.axis = 0

    def get_mean(self):
        return np.round(np.mean(self.data_array, axis=self.axis))

    def get_min(self):
        return np.min(self.data_array, axis=self.axis)

    def get_max(self):
        return np.max(self.data_array, axis=self.axis)

    def get_std(self):
        return np.round(np.std(self.data_array, axis=self.axis))

    def get_first_quartile(self):
        return np.quantile(self.data_array, .25, axis=self.axis)

    def get_second_quartile(self):
        return np.quantile(self.data_array, .50, axis=self.axis)

    def get_third_quartile(self):
        return np.percentile(self.data_array, .75, axis=self.axis)

    def count_unique_duplicate(self):
        unique_list, duplicate_list = [], []
        for i in range(len(self.headers)-1):
            elements_of_np_array, count = np.unique(self.data_array[:, i], axis=self.axis, return_counts=True)
            unique_list.append(len(elements_of_np_array[count == 1]))
            duplicate_list.append(len(elements_of_np_array[count > 1]))
        return unique_list, duplicate_list

    def get_unique(self):
        return self.count_unique_duplicate()[0]

    def get_duplicate(self):
        return self.count_unique_duplicate()[1]

    def get_outlier_percentage(self):
        inter_quartile_range = self.get_third_quartile() - self.get_first_quartile()
        upper_limit = self.get_first_quartile()-(1.5*inter_quartile_range)
        lower_limit = self.get_third_quartile()+(1.5*inter_quartile_range)
        outlier_percentage = []
        for column_values in range(len(self.headers)-1):
            counter = 0
            for row_value in self.data_array[:, column_values]:
                if (row_value > upper_limit[column_values]) | (row_value < lower_limit[column_values]):
                    counter += 1
            single_outlier_percentage = np.round((counter/len(self.data_array[:, column_values]) * 100))
            outlier_percentage.append(single_outlier_percentage)
        return outlier_percentage

