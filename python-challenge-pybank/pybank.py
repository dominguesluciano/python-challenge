# import module os
import os
# Module for reading CSV files
import csv
bank_file = os.path.join('Resources', 'budget_data.csv')

#The total number of months included in the dataset
total_mo = 1
mo_list =[]

# The net total amount of "Profit/Losses" over the entire period
profit_loss = 0

#list of changes
changes_list = []

#The greatest increase /decrease in profits (date and amount) over the entire period
greatest_increase = ["",0]
greatest_decrease = ["",999999999]

with open(bank_file, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    #set first row as actual second row of dataframe
    first_row = next(csvreader)
    last_month_change = float(first_row[1])
    sum_total_pl = 0 + last_month_change
    
    # Read each row of data after the header

    for row in csvreader:
        total_mo = total_mo +1
        profit_loss = float(row[1])
        sum_total_pl += profit_loss

        # mo_list.append(str(row[0]))
        # min_inc.append(float(row[1]))
        # max_inc.append(float(row[1]))
        #changes
        change = profit_loss - last_month_change
        changes_list.append(change)
        last_month_change = profit_loss

        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change

        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

    avg_pl = sum(changes_list)/(total_mo-1)


    #print results
   
    print(" ")
    print("Financial Analysis")
    print("----------------------------")
    print(" ")
    print(f"Total Months: {total_mo}")
    print(f"Total: ${int(sum_total_pl)}")
    print(f"Average  Change: ${round(avg_pl,2)}")
    # print(f"Greatest Increase in Profits: (${max(changes_list)})")    
    # print(f"Greatest Decrease in Profits: (${min(changes_list)})")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
   #print(f"month os min decrease is {min_inc_mo}")