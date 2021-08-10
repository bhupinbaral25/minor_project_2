from prettytable import PrettyTable
import numpy as np


def gen_table(csv_headers, stat_calc):
    stat_table = PrettyTable(csv_headers)
    stat_table.add_row(np.append(np.array(["unique"]), stat_calc.get_unique()))
    stat_table.add_row(np.append(np.array(["duplicate"]), stat_calc.get_duplicate()))
    stat_table.add_row(np.append(np.array(["mean"]), stat_calc.get_mean()))
    stat_table.add_row(np.append(np.array(["S.D"]), stat_calc.get_std()))
    stat_table.add_row(np.append(np.array(["min"]), stat_calc.get_min()))
    stat_table.add_row(np.append(np.array(["max"]), stat_calc.get_max()))
    stat_table.add_row(np.append(np.array(["25%"]), stat_calc.get_first_quartile()))
    stat_table.add_row(np.append(np.array(["50%"]), stat_calc.get_second_quartile()))
    stat_table.add_row(np.append(np.array(["75%"]), stat_calc.get_third_quartile()))
    return stat_table
