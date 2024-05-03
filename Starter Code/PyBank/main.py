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
total_profit = 0 #will hold the sum
profit = [] # this list will hold the profits for each month
index = 0
mtm_change = [] # this list will hold the month to month changes in profits

# Open the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    
    # add in the delimiter and variables that hold the contents of the file
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Reading each row in the CSV file
    for row in csvreader:
              
        month = row[0]
        profit_loss = int(row[1]) # casted values to return an integer

        # DEBUGGING -- This was to verify that the delimiter was working correctly since it was being read kind of weird
        #print(f"in {month} the profit was {profit_loss}")

        # Total months
        total_months = len(profit)
        

        # Total Profit-Losses; adding profit_loss values to each previous sum
        profitLoss = profit_loss #casts the variable to be an float so it can be summed
        profit.append(profitLoss) #currently this looks to just be creating a list--profit is a list of all the profit_loss values--worry about condensing lines later
        # profit = profit.append(int(profit_loss))
        while index < len(profit):
            total_profit = total_profit + profit[index]
            index+=1

         # Total months: counting the number of values in the list "profit" because each value in the profit list 
        total_months = len(profit)
        
        # Average Change in Profit/Losses: They want us to find the average month-to-month change; need to find month-to-month change and then average that
        average_change = total_profit/total_months

        # Greatest Increase in Profit/Losses: Once we have the average month-to-month change, then we can use the 
        greatest_increase = max(profit)
        
        
    # print values
    print(total_months)
    print(total_profit)
    print(positive)
    print(negative)
    print(average_change)
    print(greatest_increase)
    print(profit)
    print(len(profit))