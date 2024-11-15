import pandas as pd
from datetime import datetime

# Load timesheet data
timesheet = pd.read_excel("Data/payroll_timesheet.xlsx")

# Calculate total hours worked
timesheet['Total Hours'] = (
    pd.to_datetime(timesheet['Clock Out']) - pd.to_datetime(timesheet['Clock In'])
).dt.total_seconds() / 3600

# Save results to a new Excel file
timesheet.to_excel("processed_timesheet.xlsx", index=False)
print("Payroll automation complete!")
