# Module for creating files across operating systems
import os

# Module for reading CSV files
import csv

# Set path for files using relative path
csvpath = "PyPoll/Resources/election_data.csv"
outputpath = "PyPoll/Analysis/pypoll_output.txt"

#defining variables
candidates = [] # Will output the 3rd column of the CSV file

# Open the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    
    # add in the delimiter and variables that hold the contents of the file
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Reading each row in the CSV file
    for row in csvreader:
                      
        ballotid = row[0]
        county = row[1]
        candidate = row[2]

        # First create a list with just the candidates

    # Get the total_votes using len(candidates)

    # Use list comprehension to create new lists with just the candidates names
    # list stockham for all ballots cast for him
    # list degette for all ballots cast for her
    # list doane for all ballots cast for him

    # once all the lists are created
    # use len to get ballots cast for each candidate
    # divide number ballots for each candidate by total votes to get percentage of ballots cast for each person

    # create 2 lists, 1 with the votes for each candidate, 1 with the candidates names (maybe) and then output one with the most votes
    # # There is probably an easier way to do this... idk
    
