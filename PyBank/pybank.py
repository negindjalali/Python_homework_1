
import pathlib
import csv
csvpath = pathlib.Path('/Users/negindjalali/Desktop/USC/Curriculum/usc-la-virt-data-pt-06-2021-u-c/unit_03_python/homework/PyBank/Resources/budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)    
    

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    list=[]
    month = []
    total_change=[]
    average_change= []
    monthly_change=[]

    for row in csvreader:
        list.append(row[1])
        month.append(row [0])
    total = len(month)
    #print(total)
    int_list = map(int, list)
    
    profit = sum(int_list)
    #print(profit)

    
    
    i=0   
    for i in range(len(list)-1):
        delta = int(list[i+1]) - int(list[i])
       
    total_change.append(delta)
       
    average_change = sum(total_change)
              
    monthly_change= average_change/len(total_change)

    #print(monthly_change)

    greatest_increase = max(total_change)
    #print(greatest_increase)
    #print(total_change.index(greatest_increase))
    best_month= month[25]
    

    greatest_decrease = min(total_change)
    #print(greatest_decrease)
    #print(total_change.index(-2196167))
    worst_month = month[44]


    print(f"total number of months is: {total}")
    print(f"total amount of profit/loss is: ${profit}")
    print(f"The average of change in profit/losses is: ${monthly_change}")
    print(f"the greatest in increase in amount is  ${greatest_increase} in the month of {best_month}")
    print(f"the greatest in decrease in amount is  ${greatest_decrease} in the month of {worst_month}")
    


