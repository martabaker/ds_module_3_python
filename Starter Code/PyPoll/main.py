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
    # list degette for all ballots cast for her
    degette = [name for name in candidates if name == "Diana DeGette"]
     # list doane for all ballots cast for him
    doane = [name for name in candidates if name == "Raymon Anthony Doane"]
  
    # once all the lists are created
    # use len to get ballots cast for each candidate
    stockham_votes = len(stockham)
    degette_votes = len(degette)
    doane_votes = len(doane)

    # divide number ballots for each candidate by total votes to get percentage of ballots cast for each person; these values are being rounded to the 3rd decimal point for ease of reading
    stockham_perc = round((stockham_votes/total_votes) * 100,3)
    degette_perc = round((degette_votes/total_votes) * 100, 3)
    doane_perc = round((doane_votes/total_votes) * 100, 3)

    # create 2 lists, 1 with the votes for each candidate, 1 with the candidates names (maybe) and then output one with the most votes
    candidate_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"] # This list contains the names of the 3 candidates 
    vote_list = [stockham_votes, degette_votes, doane_votes] # This list contains the number of votes each candidate won
    candidate_perc = [stockham_perc, degette_perc, doane_perc] # This list contains the percent of the vote each candidate won
    winning_perc = max(candidate_perc) # This determines which candidate won the vote by getting the greatest share of the votes

    winning_cand = candidate_list[candidate_perc.index(winning_perc)] # Finding the value in the candidate_list list that corresponds to the winning percent


f = open(outputpath, "w")
f.write("Election Results\n")
f.write("------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("------------------------\n")
f.write(f"{candidate_list[0]}: {candidate_perc[0]}% ({vote_list[0]})\n")
f.write(f"{candidate_list[1]}: {candidate_perc[1]}% ({vote_list[1]})\n")
f.write(f"{candidate_list[2]}: {candidate_perc[2]}% ({vote_list[2]})\n") 
f.write("------------------------\n")
f.write(f"Winner: {winning_cand}\n")
f.write("------------------------")
f.close()

# # Print out the desired results; using a lot of variable names to try and make the result list more dynamic
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")
print(f"{candidate_list[0]}: {candidate_perc[0]}% ({vote_list[0]})")
print(f"{candidate_list[1]}: {candidate_perc[1]}% ({vote_list[1]})")
print(f"{candidate_list[2]}: {candidate_perc[2]}% ({vote_list[2]})") 
print("------------------------")
print(f"Winner: {winning_cand})")
print("------------------------")
    
