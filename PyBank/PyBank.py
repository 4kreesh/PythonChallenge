
import os
import csv

Budget_data_path = os.path.join('.','Resources','budget_data.csv') # files to load
file_to_output = os.path.join('.','budget_analysis.txt') # files to output

date_value = []
pl = []
changes = []
with open(Budget_data_path,'r') as csv_file:
    Budget_reader = csv.reader(csv_file, delimiter=",")
    header = next(Budget_reader)
    #print(header)
    
    for row in Budget_reader:
     
        date_value.append(row[0])     # adding date column to a list 
        pl.append(int(row[1]))        # adding profit/loss column to a list
        if len(pl) > 1 : changes.append(int(row[1]) - pl[-2]) # to find changes in profit/loss and condition to check the list has atleast one value 
        

# Calculations

Total_Months = len(date_value)    # Total months , using len function
Total = sum(pl) # Total
high_profit = max(changes)
high_loss = min(changes)
high_profit_index = changes.index(high_profit)
high_loss_index = changes.index(high_loss)

output = (f'Financial Analysis \n' f'---------------------------------- \n'
         f'Total Months: {Total_Months}\n' f'Total : ${Total}\n' 
         f'Average Changes : $ {round(sum(changes)/len(changes),2)}\n'
         f'Greatest Increase in Profits : {date_value[high_profit_index+1]}  ($ {high_profit})\n'
         f'Greatest Decrease in Profits : {date_value[high_loss_index+1]}  ($ {high_loss})\n')
print(output)

with open(file_to_output, 'w') as txt_file:
    txt_file.write(output)
        

