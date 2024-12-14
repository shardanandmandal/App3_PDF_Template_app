import pandas as pd

# Paths to your Excel files
file1 = "file1.xlsx"
file2 = "file2.xlsx"
file3 = "file3.xlsx"

# Load the data from each Excel file into a DataFrame
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)
df3 = pd.read_excel(file3)

# Combine the DataFrames into a single DataFrame
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Save the combined DataFrame to a new Excel file
output_file = "combined_file.xlsx"
combined_df.to_excel(output_file, index=False)

print(f"Combined data saved to {output_file}")
