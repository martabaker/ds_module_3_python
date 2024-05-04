# Module for creating files across operating systems
import os

# Module for reading CSV files
import csv

# Set path for files using relative path
csvpath = "PyBank/Resources/budget_data.csv"


#defining total_profit and lists
total_profit = 0 #will hold the sum of the profits and losses
profit = [] # this list will hold the profits and losses for each month from the CSV file
index = 0
mtm_change = {} # this dictionary will hold the month to month changes in profits and the corresponding month where they occur
change = [] # this list will hold all of the changes for the months
months = [] # this list holds all of the month data from the CSV file
only_change = [] # this list excludes the first value that was in the change file since the first value in the change list was just the first profit-loss value

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

        # Total Profit-Losses; adding profit_loss values to each previous sum
        profitLoss = profit_loss #casts the variable to be an float so it can be summed
        profit.append(profitLoss) #currently this looks to just be creating a list--profit is a list of all the profit_loss values--worry about condensing lines later

        while index < len(profit):
            total_profit = total_profit + profit[index]
            index+=1

        # Total months: counting the number of values in the list "profit" because each value in the profit list 
        total_months = len(profit)

        # to create a list of the months
        monthlist = month
        months.append(monthlist)
        

        
    
    print(total_profit)
    print(profit)
    print(months)
    print(total_months)

    # This finds the month to month changes with help from the Xpert
    for i in range(len(profit)):
        if i == 0:
            chng = profit [0]
        else:
            chng = (profit[i]-profit[i-1])
        change.append(chng)
        
    print(change)

    only_change = change.copy() # creating a copy of the change list because I need it for other work and the list is going to be emptied when creating the dictionary
    


    # This merges the months list and the change lists into a dictionary where the months are the keys and changes are the values
    # Source: https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
    for key in months:
        for value in change:
            mtm_change[key] = value
            change.remove(value)
            break
    
    # Writing code to calculate the average of the changes
    only_change.pop(0) # This removes the 1st value in the list because it isn't a change. It was just the first value in the data
    print(only_change)
    
    average_change = sum(only_change)/len(only_change) # Summing the list of changes and then dividing the number of values in the list to find the average of the changes

    greatest_increase = max(only_change)
    greatest_decrease = min(only_change)
      

        
    # print values
    # print(total_months)
    # print(total_profit)
    # print(positive)
    # print(negative)
    print(average_change)
    print(greatest_increase)
    print(greatest_decrease)
    # print(profit)
    # print(len(profit))
    print(mtm_change)


# # Print out the desired results
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change}")
    # print(f"Greatest Increase in Profits: {month} (${greatest_increase})")
    # print(f"Greatest Decrease in Profits: {month} (${greatest_decrease})")