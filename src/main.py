from handling_csv import HandlingCSV
import all_statistical_calculations
import tabulate_data
from paths import cleaned_marketing_dataset

if __name__ == '__main__':
    csv_class = HandlingCSV(cleaned_marketing_dataset)
    csv_data = csv_class.get_csv_elements()
    csv_headers = csv_class.get_csv_headers()
    stat_calc = all_statistical_calculations.StatisticalCalculations(csv_data, csv_headers)
    table = tabulate_data.gen_table(csv_headers, stat_calc)
    print(table)
