import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sarvani@1025",
    database="loan_management"
)

cursor = connection.cursor()

print("\n========== LOAN ANALYTICS ==========\n")

# Total Active Loans
cursor.execute("SELECT COUNT(*) FROM active_loans")
active_count = cursor.fetchone()[0]
print(f"Total Active Loans      : {active_count}")

# Total Released Loans
cursor.execute("SELECT COUNT(*) FROM released_loans")
released_count = cursor.fetchone()[0]
print(f"Total Released Loans    : {released_count}")

# Total Principal Amount
cursor.execute("SELECT SUM(Principal_Amount) FROM released_loans")
principal = cursor.fetchone()[0]
print(f"Total Principal Amount  : ₹ {principal:,.2f}")

# Total Interest Earned
cursor.execute("SELECT SUM(Interest_Earned) FROM released_loans")
interest = cursor.fetchone()[0]
print(f"Total Interest Earned   : ₹ {interest:,.2f}")

# Average Loan Amount
cursor.execute("SELECT AVG(Principal_Amount) FROM released_loans")
average = cursor.fetchone()[0]
print(f"Average Loan Amount     : ₹ {average:,.2f}")

# Highest Loan
cursor.execute("SELECT MAX(Principal_Amount) FROM released_loans")
highest = cursor.fetchone()[0]
print(f"Highest Loan Amount     : ₹ {highest:,.2f}")

# Lowest Loan
cursor.execute("SELECT MIN(Principal_Amount) FROM released_loans")
lowest = cursor.fetchone()[0]
print(f"Lowest Loan Amount      : ₹ {lowest:,.2f}")

print("\n===================================\n")

cursor.close()
connection.close()