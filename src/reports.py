import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sarvani@1025",
    database="loan_management"
)

# SQL Queries
active = pd.read_sql("SELECT * FROM active_loans", connection)
released = pd.read_sql("SELECT * FROM released_loans", connection)

# Analytics
summary = pd.DataFrame({
    "Metric": [
        "Total Active Loans",
        "Total Released Loans",
        "Total Principal Amount",
        "Total Interest Earned",
        "Average Loan Amount",
        "Highest Loan",
        "Lowest Loan"
    ],
    "Value": [
        len(active),
        len(released),
        released["Principal_Amount"].sum(),
        released["Interest_Earned"].sum(),
        round(released["Principal_Amount"].mean(),2),
        released["Principal_Amount"].max(),
        released["Principal_Amount"].min()
    ]
})

# Save Excel Report
output_file = "../reports/Loan_Report.xlsx"

with pd.ExcelWriter(output_file) as writer:

    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    active.to_excel(
        writer,
        sheet_name="Active Loans",
        index=False
    )

    released.to_excel(
        writer,
        sheet_name="Released Loans",
        index=False
    )

print("Loan Report Generated Successfully!")

connection.close()