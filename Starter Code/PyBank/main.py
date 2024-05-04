# Module for creating files across operating systems
import os

# Module for reading CSV files
import csv

# Set path for files using relative path
csvpath = "PyBank/Resources/budget_data.csv"
outputpath = "PyBank/Analysis/pybank_output.txt"

#defining variables
total_profit = 0 # will hold the sum of the profits and losses
profit = [] # this list will hold the profits and losses for each month from the CSV file
index = 0
change = [] # this list will hold all of the changes for the months
months = [] # this list holds all of the month data from the CSV file

# Open the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    
    # add in the delimiter and variables that hold the contents of the file
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Reading each row in the CSV file
    for row in csvreader:
              
        month = row[0]
        profit_loss = int(row[1]) # casted values to return an integer

        # Total Profit-Losses; adding profit_loss values to each previous sum
        profitLoss = profit_loss # creating a temporary variable
        profit.append(profitLoss) 

        # Adds all of the values in the profit list together to get the total profit
        while index < len(profit):
            total_profit = total_profit + profit[index]
            index+=1

        # Total months: counting the number of values in the list "profit" because each value in the profit list 
        total_months = len(profit)

        # to create a list of the months
        monthlist = month
        months.append(monthlist)
        

    # This finds the month to month changes with help from the Xpert
    for i in range(len(profit)):
        if i == 0:
            chng = profit [0]
        else:
            chng = (profit[i]-profit[i-1])
        change.append(chng)
        
    
    change.pop(0) # This removes the 1st value in the list because it isn't a change. It was just the first value in the data
    
    average_change = sum(change)/len(change) # Summing the list of changes and then dividing the number of values in the list to find the average of the changes

    greatest_increase = max(change) # Find the maximum value of the change list using the built-in max function
    month_inc = months[change.index(greatest_increase) + 1] # Finding the value in the months list that corresponds to the greatest increase. Added 1 to the index because the first value in the original change list was removed
    
    # repeated the greatest_increase work for the greatest_decrease
    greatest_decrease = min(change)
    month_dec = months[change.index(greatest_decrease) + 1]


f = open(outputpath, "w")
f.write(f"Financial Analysis\n------------------------\nTotal Months: {total_months}\nTotal: ${total_profit}\nAverage Change: ${round(average_change,2)}\nGreatest Increase in Profits: {month_inc} (${greatest_increase})\nGreatest Decrease in Profits: {month_dec} (${greatest_decrease})")
f.close()

# # Print out the desired results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${round(average_change,2)}") # Rounds this value to 2 decimal points to be more in line with normal monetary values
print(f"Greatest Increase in Profits: {month_inc} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {month_dec} (${greatest_decrease})")