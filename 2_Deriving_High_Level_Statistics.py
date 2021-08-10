import csv
import numpy as np
from prettytable import PrettyTable
try:
    def extract_from_csv(data_set):
        marketing_np_array = np.genfromtxt(data_set, dtype=np.int64, delimiter=",",
                                       skip_header=1)
        marketing_np_array = np.delete(marketing_np_array, 0, axis=1)
        return marketing_np_array
except:
    print("Error found to read data")



def check_unique_duplicate(numpy_array):
    unique_list, duplicate_list = [], []
    for i in range(13):
        unique, count = np.unique(numpy_array[:,i], axis=0, return_counts=True)
        unique_list.append(len(unique[count==1]))
        duplicate_list.append(len(unique[count>1]))
        return np.array(unique_list),np.array(duplicate_list)



if __name__ == '__main__':
    data = extract_from_csv('Dataset/cleaned_marketing_data.csv')
    print(data)

