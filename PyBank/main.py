import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_profit = 0
average_change = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Gets the header info
    csv_header = next(csvreader)

    first_row = next(csvreader)
    # initialize these variables
    greatest_profit = int(first_row[1])
    greatest_loss = int(first_row[1])

    # Loops through the rows
    for row in csvreader:
        current_profit = int(row[1])
        # keep track of # of months (this is also total number of rows)
        total_months = total_months + 1

        total_profit = total_profit + current_profit

        if (greatest_profit < current_profit):
            greatest_profit = current_profit
            profit_month = row[0]
        
        if (greatest_loss > current_profit):
            greatest_loss = current_profit
            loss_month = row[0]
         
    average_change = round(total_profit / total_months, 2)    # im pretty sure this is correct
    

print(f"Total months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {profit_month} (${greatest_profit})")
print(f"Greatest Decrease in Profits: {loss_month} (${greatest_loss})")

# Redoing all the print statements into output file
output_path = os.path.join("Results.csv")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow([f"Total months: {total_months}"])
    csvwriter.writerow([f"Total: ${total_profit}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {profit_month} (${greatest_profit})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {loss_month} (${greatest_loss})"])

