import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_profit = 0
average_change = 0
# correctly initializes these 2 variables below
greatest_profit = 0
greatest_loss = 0
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Gets the header info
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Loops through the rows
    for row in csvreader:
        current_profit = int(row[1])
        # keep track of # of months (this is also total number of rows)
        total_months = total_months + 1

        total_profit = total_profit + current_profit

        # if the current cells has greater profit than stored value OR we're just starting so initializing variables
        if (greatest_profit < current_profit) or row == 1:
            greatest_profit = current_profit
            profit_month = row[0]
        
        # if the current cells has greater loss than stored value OR we're just starting so initializing variables
        if (greatest_loss > current_profit) or row == 1:
            greatest_loss = current_profit
            loss_month = row[0]

        # trying to figure out how to call specifically the first row of data if row is not an int HMMMMM
        if row == 1:
            print(row)
            print("these should be Jan-2010,867884")


    average_change = round(total_profit / total_months, 2)    # im pretty sure this is correct way to avg but number isn't the same so hmm
    

# print(f"Total months: {total_months}")
# print(f"Total: ${total_profit}")
# print(f"Average Change: ${average_change}")
# print(f"Greatest Increase in Profits: {profit_month} (${greatest_profit})")
# print(f"Greatest Decrease in Profits: {loss_month} (${greatest_loss})")