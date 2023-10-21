import os
import csv

#credit in readme file to tutor because your paths are trash
os.chdir(os.path.dirname(os.path.realpath(__file__)))

budget_data=os.path.join('..', 'Resources', 'budget_data.csv')
with open(budget_data) as monthly_budget:
    csvreader=csv.reader(monthly_budget, delimiter=',')
    csvheader=next(csvreader)

#Calculate total number of months in the budget_data.
    #YOU NEED TO make a for loop where total months starts at 0 and each row adds 1 to that value.
    total_months as double = 0
    #is this how we define a variable in python? my brain has too much VBA in it to be anything but troublesome.
    for 
    #sophie this is WRONG. 
    print(f"The total months used in this data set is {total_months} months.")

#Calculate the net total of Profit/Losses over the entire period
    #just add up the entire profits/losses column in the csv?
    #do we need to define that column as long?
    #do we do the same thing we did up above but instead of adding 1 add the value of the column?
    net_total as int = 0

#Calculate changes in Profit/Losses over the entire period
    #define monthly_change, nextrow, current row (as long variables?)
    currentrow = 
    nextrow =
    monthly_change = nextrow-currentrow

    #make a loop to add up all the monthly_change values to = total_profit_loss_change
    #do we need a previous_monthly_change variable? am i thinking too hard?
    #do we make a third column in the csv file with this? to store it?
    total_profit_loss_change as long = 


#average those changes
    #divide total_profit_loss_change by (total_months - 1) (because there is no profit/loss change for first value)
        #do these need to be defined as the same type of variable?

#find the greatest increase in profits (date and amount) over the entire period
    #this is why i think we need to make a third column but I'm bonkers confused.

#find the greatest decrease in profits (date and amount) over the entire period

#Print the following to the terminal and export a text file with the following information.
print("Financial Analysis")
print(f"Total Months: " {total_months})
print(f"Total Profits/Losses: " {net_total})
print(f"Average Change: " {mean_monthly_change})
print(f"Greatest Increase in Profits: " {max_increase_monthly_change})
print(f"Total Profits/Losses: " {max_decrease_monthly_change})