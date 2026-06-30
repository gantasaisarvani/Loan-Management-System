import mysql.connector
import matplotlib.pyplot as plt

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sarvani@1025",
    database="loan_management"
)

cursor = connection.cursor()

# Active Loans
cursor.execute("SELECT COUNT(*) FROM active_loans")
active = cursor.fetchone()[0]

# Released Loans
cursor.execute("SELECT COUNT(*) FROM released_loans")
released = cursor.fetchone()[0]

labels = ["Active Loans", "Released Loans"]
values = [active, released]

plt.figure(figsize=(6,5))
plt.bar(labels, values)

plt.title("Loan Status")
plt.xlabel("Status")
plt.ylabel("Number of Loans")
plt.savefig("../reports/loan_status_chart.png", dpi=300, bbox_inches="tight")

plt.show()

cursor.close()
connection.close()