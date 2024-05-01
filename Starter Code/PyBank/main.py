# Module for creating files across operating systems
import os

# Module for reading CSV files
import csv

# Set path for files using relative path with slashes flipped
csvpath = "PyBank/Resources/budget_data.csv"

# Set variables

# Open the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    
    # add in the delimiter and variables that hold the contents of the file
    csvreader = csv.reader(csvfile, delimiter=",")


    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # DEBUGGING - Check to make sure it's reading the file correctly
    for row in csvreader:
        month = row[0]
        profit_loss = row[1]
        print(f"in {month} the profit was {profit_loss}")

        # Total months; added 1 to the sum to account for the first row being 0
        # Source: https://stackoverflow.com/questions/16108526/how-to-obtain-the-total-numbers-of-rows-from-a-csv-file-in-python
        total_months = (sum(1 for row in csvreader) + 1)
        print(total_months)

        # Total Profit-Losses
        total = sum(int(profit_loss))
        print(total)