import high_level_statstics as hls
import streamlit as st


data_file = "MINOR_PROJECT_2/Dataset/cleaned_marketing_data.csv"

numpy_array = hls.extract_from_csv(data_file)
headers = hls.read_header(data_file)

unique_count, dublicate_count = hls.count_unique_duplicate(numpy_array)

st.write(hls.gen_table(numpy_array, headers, unique_count, dublicate_count))

