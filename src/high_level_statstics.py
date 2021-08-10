import csv
import numpy as np
from prettytable import PrettyTable


class HandlingCSV:
    def __init__(self, data_set):
        self.data_set = data_set

    def get_csv_elements(self):
        try:
            marketing_np_array = np.genfromtxt(self.data_set, dtype=np.int64, delimiter=",")
            marketing_np_array = np.delete(marketing_np_array, 0, axis=1)
            print(marketing_np_array.dtype)
        except Exception as exp:
            print("Exception:{}".format(exp))
        else:
            return marketing_np_array

    def get_csv_headers(self):
        try:
            with open(self.data_set, 'r') as file:
                my_reader = csv.reader(file, delimiter=',')
                headers_list = next(my_reader, None)
        except Exception as exp:
            print("Exception:{}".format(exp))
        else:
            return headers_list


# def count_unique_duplicate(numpy_array):
#     unique_list, duplicate_list = [], []
#     row, column = numpy_array.size
#     for i in range(column):
#         unique, count = np.unique(numpy_array[:, i], axis=0, return_counts=True)
#         unique_list.append(len(unique[count == 1]))
#         duplicate_list.append(len(unique[count > 1]))
#         return np.array(unique_list), np.array(duplicate_list)
#
#
# def gen_table(numpy_array, header, unique_count, duplicate_count):
#     stat_table = PrettyTable(header)
#     stat_table.add_row(np.append(np.array(["unique"]), unique_count))
#     stat_table.add_row(np.append(np.array(["duplicate"]), duplicate_count))
#     stat_table.add_row(np.append(np.array(["mean"]), np.mean(numpy_array, axis=0)))
#     stat_table.add_row(np.append(np.array(["S.D"]), np.std(numpy_array, axis=0)))
#     stat_table.add_row(np.append(np.array(["min"]), np.min(numpy_array, axis=0)))
#     stat_table.add_row(np.append(np.array(["max"]), np.max(numpy_array, axis=0)))
#     stat_table.add_row(np.append(np.array(["25%"]), np.percentile(numpy_array, 25, axis=0)))
#     stat_table.add_row(np.append(np.array(["50%"]), np.percentile(numpy_array, 50, axis=0)))
#     stat_table.add_row(np.append(np.array(["75%"]), np.percentile(numpy_array, 75, axis=0)))
#     return stat_table



