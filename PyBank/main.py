#
#Author: @Alex Feeney
#

#import csv required for using csv file
import csv

#open csv resoure file to read in data and store it in file_obj
with open('Resources/budget_data.csv') as file_obj: 
    
    #set a counter to sign a row
    row_counter = 0 
    
    #set variables to keep track of the greatest increase and decrease. 
    greatestIncrease = 0 
    greatestDecrease = 0 
    greatestIncreaseDate = ''
    greatestDecreaseDate = ''
    
    #set variables for calculating the average change between months
    revAverage = 0 
    revChange = 0 
    revChangeList = []
    prevRevenue = 0 
    
    #set total to keep track of the total profit/loss in file. 
    total = 0 
    
    #create a reader object to read data
    readerObj = csv.reader(file_obj)
    
    #store header row into csvHeader
    csvHeader = next(readerObj)
    
    previousRow = 0
    
    #loop over rows
    for row in readerObj: 
       
       #add to total amount 
       total += int(row[1])
       
       #count the number of records
       row_counter +=1
       
       #calculate the difference in revenue from the last month (only words as the rows are sorted in month desc order)
       revChange = float(row[1]) - prevRevenue
       
       #assign previous months revenue for next loops 
       prevRevenue = float(row[1])
       
       #add revenue change to list to later divide
       revChangeList.append(revChange)
       
              
      #check if the change is greater than the top increase and assign if greater than
       if revChange > greatestIncrease:
           greatestIncrease = revChange
           greatestIncreaseDate = row[0]
           
       #check if the change is less than the top descrease and assign if less than     
       if revChange < greatestDecrease: 
           greatestDecrease = revChange
           greatestDecreaseDate = row[0]
           
       print(row)
           
    revAverage = sum(revChangeList)/len(revChangeList)
print(revChangeList)
#output results to terminal
print("""
Financial Analysis

---------------------------------------------------
""")
print(f'Total Months: {row_counter} \n')
print(f'Total: ${total}\n')
print(f'Average Change: ${revAverage} \n')
print(f'Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease}) \n')
print(f'Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease}) \n')

#output results to text log file. 





