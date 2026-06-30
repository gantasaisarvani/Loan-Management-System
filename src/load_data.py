import pandas as pd

# Excel file path
file_path = "../loan_records.xlsx"

# Read all sheets
excel_data = pd.read_excel(file_path, sheet_name=None)

# Display sheet names
print("Sheets in the Excel file:")
print(excel_data.keys())

# Read individual sheets
active_df = excel_data["Active"]
released_df = excel_data["released"]
merged_df = excel_data["Merge_Data"]
active_df.rename(columns={"0": "Interest_Rate"}, inplace=True)

# Display first 5 rows
print("\n===== Active Loans =====")
print(active_df.head())

print("\n===== Released Loans =====")
print(released_df.head())

print("\n===== Merged Data =====")
print(merged_df.head())

print("\nMissing Values in Active Sheet")
print(active_df.isnull().sum())

print("\nMissing Values in Released Sheet")
print(released_df.isnull().sum())

print("\nMissing Values in Merged Sheet")
print(merged_df.isnull().sum())

print("\nDuplicate Rows in Active:", active_df.duplicated().sum())

print("Duplicate Rows in Released:", released_df.duplicated().sum())

print("Duplicate Rows in Merged:", merged_df.duplicated().sum())

print("\n===== Active Data Types =====")
print(active_df.dtypes)

print("\n===== Released Data Types =====")
print(released_df.dtypes)

print("\n===== Merged Data Types =====")
print(merged_df.dtypes)