from high_level_statstics import HandlingCSV
import all_statistical_calculations
import tabulate_data

data_set = '../dataset/cleaned_marketing_data.csv'


if __name__ == '__main__':
    csv_class = HandlingCSV(data_set)
    csv_data = csv_class.get_csv_elements()
    csv_headers = csv_class.get_csv_headers()
    stat_calc = all_statistical_calculations.StatisticalCalculations(csv_data, csv_headers)
    table = tabulate_data.gen_table(csv_headers, stat_calc)
    print(table)
