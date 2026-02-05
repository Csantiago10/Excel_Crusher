import pandas as pd
import os


# 1.  setting paths for the input and output folders
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_folder = os.path.join(base_dir, "input_data")
output_folder = os.path.join(base_dir, "output_data")

# 2. Get list of files in the input folder
files = os.listdir(input_folder)

# 3. List for save the dataframes
all_dfs = []


print(f"Searchs files in: {input_folder}")

for filename in files:

    # A. Validate that the files is a excel file (.xlsx)
    if not filename.endswith(".xlsx"):
        continue

    # B. Build the full path of the file
    file_path = os.path.join(input_folder, filename)

    try:
        # C. Read the file
        print(f"Proccesing file: {filename}")
        df_temp = pd.read_excel(file_path)

        # D. Create a column with the name of the file original
        df_temp['Source_File'] = filename

        # E. Append the dataframe to the list
        all_dfs.append(df_temp)

    except Exception as e:
        print(f"Error processing file {filename}: {e}")
        

# 4. Concatenate all dataframes
if all_dfs:
    print("Concatenating dataframes...")

    # ignore_index=True is vital for reboot the number of rows (0, 1, 2, 3...)
    master_df = pd.concat(all_dfs, ignore_index=True)

    # 5. Export the master dataframe to the output folder
    output_path = os.path.join(output_folder, "MASTER_REPORT.xlsx")
    master_df.to_excel(output_path, index=False)

    print(f"✅ ¡Éxito! Master Report save in: {output_folder}")
    print(f"Total rows: {len(master_df)}")

else:
    print("⚠️ No found files excel to concatenate.")