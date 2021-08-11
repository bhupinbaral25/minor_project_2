
# import streamlit as st
# import pandas as pd
# import high_level_statstics as hls


# data_file = "cleaned_marketing_data.csv"
#
# numpy_array = ut.extract_from_csv(data_file)
# headers = ut.read_header(data_file)
# df = pd.read_csv("cleaned_marketing_data.csv")
#
# unique_count, dublicate_count = ut.count_unique_duplicate(numpy_array)

# st.write(ut.gen_table(numpy_array, headers, unique_count, dublicate_count))
#
# dataframe = pd.DataFrame.from_dict(hls.calculate_statstics(numpy_array))
#
# st.write(dataframe)