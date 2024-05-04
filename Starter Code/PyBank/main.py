# Module for creating files across operating systems
import os

# Module for reading CSV files
import csv

# Set path for files using relative path
csvpath = "PyBank/Resources/budget_data.csv"


#defining total_profit and lists
total_profit = 0 #will hold the sum
profit = [] # this list will hold the profits for each month
index = 0
#mtm_change = [] # this list will hold the month to month changes in profits
# change = []
# mtm_dict = {}

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

        # Total months
        total_months = len(profit)
                

        # Total Profit-Losses; adding profit_loss values to each previous sum
        profitLoss = profit_loss
        profit.append(profitLoss) #currently this looks to just be creating a list--profit is a list of all the profit_loss values--worry about condensing lines later
        
        while index < len(profit):
            total_profit = total_profit + profit[index]
            index += 1

        
        # Total months: counting the number of values in the list "profit" because each value in the profit list 
        #total_months = len(profit)
        
        mtm_change = [row for row in csvreader] # might be helpful when adding new values into dictionary   
         
    # This finds the month to month changes
    # for i in range(len(profit)):
    #     if i == 0:
    #         chng = profit [0]
    #     else:
    #         chng = (profit[i]-profit[i-1])
    #     change.append(chng)
        
        # Average Change in Profit/Losses: They want us to find the average month-to-month change; need to find month-to-month change and then average that
        #index = 0 #reseting index
        # created the dictionary from values in the csv file; help from https://saturncloud.io/blog/how-to-convert-a-csv-file-to-a-dictionary-in-python-using-the-csv-and-pandas-modules/
    
    # months = []

    # for i in range(len(profit)):
    #     months.append(month[i])

    # print(month)

    # print(mtm_change)

    #for key in 

    # temp = 0 #resetting this
    # for key in mtm_change:
    #     mtm_change[key] = change[int(temp)]
    #     temp += 1

        # while index < len(profit):
        #     mtm_change.append((profit[index]-profit[index-1]))
        #     index+=1
        

        # Greatest Increase in Profit/Losses: Once we have the average month-to-month change, then we can use the 
        #greatest_increase = max(profit)
        
        
    # print values
    # print(total_months)
    print(total_profit)
    # print(positive)
    # print(negative)
    # print(average_change)
    # print(greatest_increase)
    #print(mtm_change)
    
    # print(len(profit))
    #print(change,change1)


# # Print out the desired results
    # print("Financial Analysis")
    # print("------------------------")
    # print(f"Total Months: {total_months}")
    # print(f"Total: ${total_profit}")
    # print(f"Average Change: ${average_change}")
    # print(f"Greatest Increase in Profits: {month} (${greatest_increase})")
    # print(f"Greatest Decrease in Profits: {month} (${greatest_decrease})")