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
    total_months=0
    total_profits_losses=0
    total_monthly_difference=0
    max_increase_monthly_change=0
    max_decrease_monthly_change=0
    increase_month=""
    decrease_month=""

    for rownum in csvreader:
        #adding one to total months, reassigning it
        total_months = total_months+1

        total_profits_losses = total_profits_losses+int(rownum[1])
       
        #so it doesn't calculate difference for first number
        if total_months>1:
            total_monthly_difference=total_monthly_difference+int(rownum[1])-previous_month_value
            
            current_monthly_change=int(rownum[1])-previous_month_value
            if current_monthly_change>max_increase_monthly_change:
                max_increase_monthly_change=current_monthly_change
                increase_month=rownum[0]

            if current_monthly_change<max_decrease_monthly_change:
                max_decrease_monthly_change=current_monthly_change
                decrease_month=rownum[0]
            
        #keep the previous_month_value at the bottom because python reads top to bottom and it will not change before it is used to calculate total_monthly_differnece_
        previous_month_value = int(rownum[1])


#Print the following to the terminal and export a text file with the following information.

print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total Profits/Losses: {total_profits_losses}")
print(f"Average Change: ${(round(total_monthly_difference/(total_months-1), 2))}")
print(f"Greatest Increase in Profits: {increase_month}, ${max_increase_monthly_change}")
print(f"Greatest Decrease in Profits: {decrease_month}, ${max_decrease_monthly_change}")