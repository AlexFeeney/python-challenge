#
#Author: @Alex Feeney
#
import csv

with open('Resources/budget_data.csv') as file_obj: 
    
    #start with -1 to not count head row 
    row_counter = -1 
    reader_obj = csv.reader(file_obj)
    
    for row in reader_obj: 
        #count the number of records
        row_counter +=1
        print(row)
    





#output
print("""
Financial Analysis

---------------------------------------------------
""")

print(f'Total Months: {row_counter} \n')
print('Average Change: \n')
print('Greatest Increase in Profits: \n')
print('Greatest Decrease in Profits: \n')