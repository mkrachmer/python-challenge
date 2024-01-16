# PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# -- The total number of months included in the dataset
# -- The net total amount of "Profit/Losses" over the entire period
# -- The changes in "Profit/Losses" over the entire period, and then the average of those changes
# -- The greatest increase in profits (date and amount) over the entire period
# -- The greatest decrease in profits (date and amount) over the entire period
# Your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

# identify dataset (includes 2 columns: "Date" and "Profit/Losses")
csvpath = os.path.join('Resources', 'budget_data.csv')

# initialize variables
month_count = 0
total_profit = 0
last_profit = 1088983

# create lists
profit_changes = []
date = []

# open and read csv file
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the header row 
    csv_header = next(csvfile)  

    # read through each row of data after the header
    for row in csvreader:
        # determine total number of months
        month_count = month_count + 1

        # calculate net total amount of profit/losses over entire period (assume all 3 years)
        total_profit = total_profit + int(row[1])

        # sum changes in profit/losses over the entire period by month, 
        # then store in a list to be able to calculate average, greatest increase and decrease
        current_profit = int(row[1])
        profit_change = int(current_profit) - int(last_profit)
        profit_changes.append(profit_change)
        # store dates in list to return with greatest increase/decrease profit change
        date.append(row[0])
        
        # calculate monthly profit
        last_profit = current_profit

    # calculate the average profit/loss change after exiting for loop
    avg_profit_change = ((sum(profit_changes)) / (month_count - 1))

    # determine the greatest INCREASE in profits (date and amount) over the entire period
    greatest_increase = max(profit_changes)
    increase_date = date[profit_changes.index(greatest_increase)]
   
    # determine the greatest DECREASE in profits (date and amount) over the entire period
    greatest_decrease = min(profit_changes)
    decrease_date = date[profit_changes.index(greatest_decrease)]
 
# print to terminal    
print("\n" + "Financial Analysis")
print("______________________" + "\n")
print("Total Months: " + str(month_count) + "\n")
print("Total: " + "$" + str(total_profit) + "\n")
print("Average Change: " + "$" + (str(round(avg_profit_change, 2))) + "\n")
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")" + "\n")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")" + "\n")

# print to new text file
output_path = os.path.join('analysis', 'challenge_analysis.csv')

# how to write text file: https://www.pythontutorial.net/python-basics/python-write-text-file/
#open the output file in write mode. 
with open(output_path, 'w') as textfile:
    textfile.write("\n" + "Financial Analysis" + "\n\n")
    textfile.write("______________________" + "\n\n")
    textfile.write("Total Months: " + str(month_count) + "\n\n")
    textfile.write("Total: " + "$" + str(total_profit) + "\n\n")
    textfile.write("Average Change: " + "$" + (str(round(avg_profit_change, 2))) + "\n\n")
    textfile.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")" + "\n\n")
    textfile.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")" + "\n\n")
                   
