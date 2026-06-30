import subprocess

print("=" * 50)
print("LOAN MANAGEMENT SYSTEM")
print("=" * 50)

print("\nLoading Data...")
subprocess.run(["python3", "load_data.py"])

print("\nCleaning Data...")
subprocess.run(["python3", "clean_data.py"])

print("\nLoading Data into Database...")
subprocess.run(["python3", "database.py"])

print("\nGenerating Analytics...")
subprocess.run(["python3", "analytics.py"])

print("\nGenerating Charts...")
subprocess.run(["python3", "charts.py"])

print("\nGenerating Report...")
subprocess.run(["python3", "reports.py"])

print("\nProject Executed Successfully!")