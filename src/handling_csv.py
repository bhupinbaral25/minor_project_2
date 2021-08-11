import csv
import numpy as np


class HandlingCSV:
    def __init__(self, data_set):
        self.data_set = data_set

    def get_csv_elements(self):
        try:
            marketing_np_array = np.genfromtxt(self.data_set, dtype=np.int64, delimiter=",", skip_header=True)
            marketing_np_array = np.delete(marketing_np_array, 0, axis=1)
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







