import csv
import numpy as np


class HandlingCSV:
    """
    :param data_set_path: path of the csv file
    :function get_csv_elements: returns numpy array of csv elements without headers
    :function get_csv_header returns: returns a list of headers of provided csv file
    """
    def __init__(self, data_set_path):
        self.data_set_path = data_set_path

    def get_csv_elements(self):
        try:
            marketing_np_array = np.genfromtxt(self.data_set_path, dtype=np.int64, delimiter=",", skip_header=True)
            marketing_np_array = np.delete(marketing_np_array, 0, axis=1)
            return marketing_np_array
        except Exception as exp:
            print("Exception:{}".format(exp))

    def get_csv_headers(self):
        try:
            with open(self.data_set_path, 'r') as file:
                my_reader = csv.reader(file, delimiter=',')
                headers_list = next(my_reader, None)
                return headers_list
        except Exception as exp:
            print("Exception:{}".format(exp))








