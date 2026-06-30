import pandas as pd

# Read Excel file
file_path = "../loan_records.xlsx"
excel_data = pd.read_excel(file_path, sheet_name=None)

# Read sheets
active_df = excel_data["Active"]
released_df = excel_data["released"]
merged_df = excel_data["Merge_Data"]

# Rename incorrect column
active_df.rename(columns={"0": "Interest_Rate"}, inplace=True)

# Remove extra spaces from column names
active_df.columns = active_df.columns.str.strip()
released_df.columns = released_df.columns.str.strip()
merged_df.columns = merged_df.columns.str.strip()

# Check missing values
print("\nMissing Values")
print(active_df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:", active_df.duplicated().sum())

print("\nData Cleaning Completed Successfully!")

# Convert Release_Date to datetime
released_df["Release_Date"] = pd.to_datetime(
    released_df["Release_Date"],
    errors="coerce"
)

merged_df["Release_Date"] = pd.to_datetime(
    merged_df["Release_Date"],
    errors="coerce"
)

# Convert Interest_Earned to numeric
released_df["Interest_Earned"] = pd.to_numeric(
    released_df["Interest_Earned"],
    errors="coerce"
)

merged_df["Interest_Earned"] = pd.to_numeric(
    merged_df["Interest_Earned"],
    errors="coerce"
)

print("\n===== Updated Data Types =====")
print(merged_df.dtypes)