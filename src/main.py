from high_level_statstics import HandlingCSV


data_set = '../dataset/cleaned_marketing_data.csv'


if __name__ == '__main__':
    csv_class = HandlingCSV(data_set)
    csv_data = csv_class.get_csv_elements()
    # csv_headers = csv_class.get_csv_headers()
