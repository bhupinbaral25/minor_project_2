import pandas as pd


marketingData = "Dataset/marketing_data.csv"


class CleanDataset:
    def __init__(self):
        pass

    @staticmethod
    def read_dataset(marketing_data):
        try:
            df = pd.read_csv(marketing_data)
        except FileNotFoundError:
            print("File not found.")
        except Exception as exp:
            print("Exception:{}".format(exp))
        else:
            return df






