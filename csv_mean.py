import os
import pandas as pd

directory ="/home/esma/workspace/SDF_TO_MOBLEY_v3"

file_count = 0
max_files = 10

columns = []

for filename in os.listdir(directory):
    if filename.endswith(".csv") and file_count < max_files:
        filepath = os.path.join(directory, filename)
    
        df = pd.read_csv(filepath)
        last_column = df.iloc[:, -1]
        columns.append(last_column)
        last_column.name = f"{filename.split('.csv')[0]}_last_column"
        
        file_count += 1

merged_df = pd.concat(columns, axis = 1)
merged_df["mean"] = merged_df.mean(axis=1)
merged_df.to_csv("merged_last_columns.csv", index=False)




