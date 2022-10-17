#opening the data file.
import os
import csv

#open file
budget_csv = os.path.join("Resources", "budget_data.csv") 

#initialize accumulators and variables
p_l_data = []
months=0
net_rev=0
hi_rev=0
low_rev=0

#Read in budget data
with open(budget_csv) as csvfile:
    reader = csv.reader(csvfile)
    # Read the header row
    header = next(reader)

    #read in budget data
    first_row = next(reader)
    p_l_data.append(first_row)
   
    for first_row in reader:
        p_l_data.append(first_row)

    #accumulators and hi/low

    for row in p_l_data:
        months = months + 1
        
        net_rev += int(row[1])
        
        if hi_rev < int(row[1]):
            hi_rev = int(row[1])
            hi_month = row[0]
        
        if low_rev > int(row[1]):
            low_rev = int(row[1])
            low_month = row[0]

print(" ")
print("                            FINANCIAL ANALYSIS")
print(" ")
print("--------------------------------------------------------------------------------")
print(" ")
print("                   Total Months: ", months)
print(" ")
print("                   Net Total Revenue: ", net_rev)
print(" ")
print("                   Average Monthly Revenue: ", net_rev/months)
print(" ")
print("                   Greatest Increase in Profits: ", hi_month, " ", hi_rev)
print(" ")
print("                   Greatest Decrease in Profts: ", low_month, " ", low_rev)
print(" ")

#zippity doo da...
final_numbers = zip(months, net_rev, hi_month, hi_rev, low_month, low_rev)