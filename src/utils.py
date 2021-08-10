
import csv
import numpy as np
from prettytable import PrettyTable
def extract_from_csv(data_set):
    # Read CSV using NumPy array
    try:
        marketing_np_array = np.genfromtxt(data_set, dtype=np.int64, delimiter=",",
                                       skip_header=1)
        marketing_np_array = np.delete(marketing_np_array, 0, axis=1)
        return marketing_np_array 

    except FileNotFoundError as error_message:
        #import pdb;pdb.set_trace()
        print(error_message)

def read_header(data_file):
    try:
        with open(data_file, 'r') as file:
            my_reader = csv.reader(file, delimiter=',')
            return(next(my_reader, None))

    except FileNotFoundError as error_message:
        #import pdb;pdb.set_trace()
        print(error_message)

    



def count_unique_duplicate(numpy_array):
    unique_list, duplicate_list = [], []
    column = np.size(numpy_array,1)
    
    for i in range(column):
        unique, count = np.unique(numpy_array[:,i], axis=0, return_counts=True)
        unique_list.append(len(unique[count==1]))
        duplicate_list.append(len(unique[count>1]))
        return np.array(unique_list),np.array(duplicate_list)

def gen_table(numpy_array, header, unique_count, duplicate_count):
    stat_table = PrettyTable(header)
    #stat_table.add_row(np.append(np.array(["unique"]), unique_count))
    #stat_table.add_row(np.append(np.array(["duplicate"]), duplicate_count))
    stat_table.add_row(np.append(np.array(["mean"]), np.mean(numpy_array, axis=0)))
    stat_table.add_row(np.append(np.array(["S.D"]), np.std(numpy_array, axis=0)))
    stat_table.add_row(np.append(np.array(["min"]), np.min(numpy_array, axis=0)))
    stat_table.add_row(np.append(np.array(["max"]), np.max(numpy_array, axis=0)))
    stat_table.add_row(np.append(np.array(["25%"]), np.percentile(numpy_array, 25, axis=0)))
    stat_table.add_row(np.append(np.array(["50%"]), np.percentile(numpy_array, 50, axis=0)))
    stat_table.add_row(np.append(np.array(["75%"]), np.percentile(numpy_array, 75, axis=0)))
    return stat_table


# if __name__ == '__main__':
#     data = extract_from_csv('Dataset/cleaned_marketing_data.csv')
#     print(data)

