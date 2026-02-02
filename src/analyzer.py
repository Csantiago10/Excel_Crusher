import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path_pro = os.path.join(base_dir, "input_data", "sales_data.xlsx")

print(f"Read archive from: {file_path_pro}")



df = pd.read_excel(file_path_pro)

df["Total"] = df["Quantity"] * df["Price"]

sales_day = df["Total"].sum()
# PATH for the folder output_data


path_file_out = os.path.join(base_dir, "output_data", "sales_report.xlsx")

df.to_excel(path_file_out, index=False)

print(df)

print(f"Total sales of the day: {sales_day}") # print(sales_day)