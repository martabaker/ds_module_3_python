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
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    # DEBUGGING - Check to make sure it's reading the file correctly
    for row in csv_reader:
        print(csv_reader)