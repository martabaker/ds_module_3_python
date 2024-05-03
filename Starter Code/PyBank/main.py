# Module for creating files across operating systems
import os

# Module for reading CSV files
import csv

# Set path for files using relative path with slashes flipped
csvpath = "PyBank/Resources/budget_data.csv"

# Set variables and create equations to solve the problems
# def analysis (budget):
#     month = str(budget[0]) # making sure to know this is a string -- MIGHT NOT NEED THIS
#     profit_losses = int(budget[1]) # casting this to make sure math can be done with this


# # Count the number of lines -- this might need to be solved within the open file
#     total_months = sum(1 for budget in open('PyBank/Resources/budget_data.csv')) - 1

# # Sum up the Profit/Losses
#     total_profit = sum(2 for budget in open('PyBank/Resources/budget_data.csv'))
    

# # Average Change in Profit/Losses
#     average_change = total_profit/total_months

# # # Find the Greatest Increase in profits and corresponding month
# #     greatest_increase = #type code here

# # # Find the Greatest Decrease in profits and corresponding month
# #     greatest_decrease = #type code here

# # Print out the desired results
#     print("Financial Analysis")
#     print("------------------------")
#     print(f"Total Months: {total_months}")
#     print(f"Total: ${total_profit}")
#     print(f"Average Change: ${average_change}")
#     # print(f"Greatest Increase in Profits: {month} (${greatest_increase})")
#     # print(f"Greatest Decrease in Profits: {month} (${greatest_decrease})")



#defining total_profit
total_profit=0

# Open the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    
    # add in the delimiter and variables that hold the contents of the file
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #total = 0 #Setting the initial value for total profit-loss at 0

    # Reading each row in the CSV file
    # NOTE: CURRENTLY THE PROFIT-LOSS STUFF WORKS IF THE THE TOTAL MONTHS ISN'T BEING RUN
    for row in csvreader:
              
        month = row[0]
        profit_loss = row[1] #returns a string

        # DEBUGGING -- This was to verify that the delimiter was working correctly since it was being read kind of weird
        #print(f"in {month} the profit was {profit_loss}")

        # Total months; added 1 to the sum to account for the first row being 0
        # Source: https://stackoverflow.com/questions/16108526/how-to-obtain-the-total-numbers-of-rows-from-a-csv-file-in-python NEED TO ADD TO READ ME
        #global total_months #Makes it so the total_months variable can be printed outside this code
        total_months = (sum(1 for row in csvreader) + 1)
        print(total_months)

        # Total Profit-Losses
        profitLoss = int(profit_loss) #casts the variable to be an float so it can be summed
        total_profit += profitLoss
        
        print(total_profit)