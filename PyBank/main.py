#Import modules needed to read csv files
import os
import csv


#Line 6 code courtesy of Tutor Kourt Bailey.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#open and name the csv file and data within
budget_data=os.path.join('..', 'Resources', 'budget_data.csv')
with open(budget_data) as monthly_budget:
    csvreader=csv.reader(monthly_budget, delimiter=',')
    csvheader=next(csvreader)

#For Loop starting variable definitions
    total_months=0
    total_profits_losses=0
    total_monthly_difference=0
    max_increase_monthly_change=0
    max_decrease_monthly_change=0
    increase_month=""
    decrease_month=""

    for rownum in csvreader:

        #calculating the total number of months in budget_data
        total_months = total_months+1

        #calculating the total profits/losses in the whole csv file
        total_profits_losses = total_profits_losses+int(rownum[1])
       
        #create a conditional for calculating the monthly difference in profits/losses and the average difference in profits/losses
        # ignore the difference between the starting value of total_monthly_difference and the first profits/loss number.
        if total_months>1:
            total_monthly_difference=total_monthly_difference+int(rownum[1])-previous_month_value
            
            #store the number of the current_monthly_change so it can be compared to the 
            #current max_increase_monthly_change number and max_decrease_monthly_change number
            current_monthly_change=int(rownum[1])-previous_month_value

            #change the max increase if the current_monthly_difference value is greater.
            if current_monthly_change>max_increase_monthly_change:
                max_increase_monthly_change=current_monthly_change
                increase_month=rownum[0]

            #change the max decrease if the current_monthly_difference value is greater.
            if current_monthly_change<max_decrease_monthly_change:
                max_decrease_monthly_change=current_monthly_change
                decrease_month=rownum[0]
            
        #create a variable to hold the previous month value
        # keep the previous_month_value at the bottom because python reads top to bottom and it will not change before it is used
        # to calculate total_monthly_differnece_
        previous_month_value = int(rownum[1])

#Round Average Change
rounded_average_change=(round(total_monthly_difference/(total_months-1), 2))

#Print to Terminal
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total Profits/Losses: {total_profits_losses}")
print(f"Average Change: $ {rounded_average_change}")
print(f"Greatest Increase in Profits: {increase_month}, $ {max_increase_monthly_change}")
print(f"Greatest Decrease in Profits: {decrease_month}, $ {max_decrease_monthly_change}")

#Create, open, and write a text file 
#(code courtesy of https://www.w3schools.com/python/python_file_write.asp)
f=open("PyBank_Analysis.txt", "a")
f.write("Financial Analysis \n")
f.write(f"Total Months: {total_months} \n")
f.write(f"Total Profits/Losses: {total_profits_losses} \n")
f.write(f"Average Change: $ {rounded_average_change} \n")
f.write(f"Greatest Increase in Profits: {increase_month}, $ {max_increase_monthly_change} \n")
f.write(f"Greatest Decrease in Profits: {decrease_month}, $ {max_decrease_monthly_change}")
f.close()

