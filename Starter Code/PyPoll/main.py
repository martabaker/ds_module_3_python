# Module for creating files across operating systems
import os

# Module for reading CSV files
import csv

# Set path for files using relative path
csvpath = "PyPoll/Resources/election_data.csv"
outputpath = "PyPoll/Analysis/pypoll_output.txt"

#defining variables
candidates = [] # Will output the 3rd column of the CSV file 
index = 0
stockham = [] # Will house all items in the candidates list that contain votes for Charles Casper Stockham
degette = [] # Will house all items in the candidates list that contain votes for Diana DeGette
doane = [] # Will house all items in the candidates list that contain votes for Raymon Anthony Doane

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
        candid = candidate # creating a temporary variable
        candidates.append(candid)

    # Using the length of the list "Candidates" because each item in the list corresponds to a different Ballot ID
    total_votes = len(candidates)

    # Use list comprehension to create new lists with just the candidates names
    # list stockham for all ballots cast for him
    stockham = [name for name in candidates if name == "Charles Casper Stockham"]
    print(len(stockham))
    # list degette for all ballots cast for her
    degette = [name for name in candidates if name == "Diana DeGette"]
    print(len(degette))
    # list doane for all ballots cast for him
    doane = [name for name in candidates if name == "Raymon Anthony Doane"]
    print(len(doane))

    # once all the lists are created
    # use len to get ballots cast for each candidate
    stockham_votes = len(stockham)
    degette_votes = len(degette)
    doane_votes = len(doane)

    # divide number ballots for each candidate by total votes to get percentage of ballots cast for each person
    stockham_perc = round((stockham_votes/total_votes) * 100,3)
    degette_perc = round((degette_votes/total_votes) * 100, 3)
    doane_perc = round((doane_votes/total_votes) * 100, 3)

    print(stockham_perc, degette_perc, doane_perc)

    

    # create 2 lists, 1 with the votes for each candidate, 1 with the candidates names (maybe) and then output one with the most votes
    # # There is probably an easier way to do this... idk
    
