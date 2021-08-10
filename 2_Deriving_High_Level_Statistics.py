import csv
import numpy as np


def extract_from_csv():
    marketing_np_array = np.genfromtxt('Dataset/cleaned_marketing_data.csv', dtype=np.int64, delimiter=",",
                                       skip_header=1)
    marketing_np_array = np.delete(marketing_np_array, 0, axis=1)
    return marketing_np_array


if __name__ == '__main__':
    data = extract_from_csv()
    print(data)
