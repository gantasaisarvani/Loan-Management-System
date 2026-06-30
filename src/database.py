import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sarvani@1025",
    database="loan_management"
)

if connection.is_connected():
    print("Connected to MySQL Successfully!")
    cursor = connection.cursor()

# Read Excel file
file_path = "../loan_records.xlsx"

excel_data = pd.read_excel(file_path, sheet_name=None)

active_df = excel_data["Active"]
released_df = excel_data["released"]

# Rename column
active_df.rename(columns={"0": "Interest_Rate"}, inplace=True)
active_df.rename(columns={"0": "Interest_Rate"}, inplace=True)

# SQL Query
active_query = """
INSERT INTO active_loans
(Active_ID, Loan_Date, Customer_Name, Amount, Interest_Rate, Status)
VALUES (%s, %s, %s, %s, %s, %s)
"""
# Insert Active Loan Records
for index, row in active_df.iterrows():
    cursor.execute(
        active_query,
        (
            row["Active_ID"],
            row["Dates"],
            row["Customer Name"],
            row["Amount"],
            row["Interest_Rate"],
            row["Status"],
        ),
    )
    # SQL Query for Released Loans
released_query = """
INSERT INTO released_loans
(Book_No, Loan_Date, Release_Date, Customer_Name,
Principal_Amount, Interest_Rate, Interest_Earned, Status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# Insert Released Loan Records
for index, row in released_df.iterrows():
    cursor.execute(
        released_query,
        (
            row["Book_No"],
            row["Loan_Date"],
            row["Release_Date"],
            row["Customer_Name"],
            row["Principal_Amount"],
            row["Interest_Rate"],
            row["Interest_Earned"],
            row["Status"],
        ),
    )
connection.commit()

print("Data Inserted Successfully!")

cursor.close()

connection.close()