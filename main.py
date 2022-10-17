#opening the data file.
import os
import csv

#open file
election_csv = os.path.join("Resources", "election_data.csv") 

#initialize counters and variables
election_data = []
votes = 0
total_votes=0
votes_stockham=0
votes_degette=0
votes_doane=0
first_row =0
prct_stockham = 0
prct_degette = 0
prct_doane = 0

with open(election_csv) as csvfile:
    reader = csv.reader(csvfile)
    # Read the header row
    header = next(reader)
    
    #read in election data
    first_row = next(reader)
    election_data.append(first_row)

    for first_row in reader:
        election_data.append(first_row)

    #data analysis
    
    for row in election_data:
        votes=votes+1

        
        if row[2] == "Charles Casper Stockham":
            
            votes_stockham = votes_stockham + 1

        elif row[2] == "Diana DeGette":
            votes_degette = votes_degette + 1

        else:
            votes_doane = votes_doane +1
prct_stockham = votes_stockham/votes
prct_degette = votes_degette/votes
prct_doane = votes_doane/votes

if prct_degette > prct_doane and prct_degette > prct_stockham:
    winner = "Diana DeGette"

elif prct_doane > prct_stockham:
    winner = "Anthony Doane"

else:
    winner = "Charles Casper Stockham"

#for row in election_data:
#    print(election_data)
print("")
print("                    ELECTION RESULTS")
print("------------------------------------------------")
print(f"Total Votes: {votes}")
print("------------------------------------------------")

print(f"Charles Casper Stockham: {round(prct_stockham*100,3)}%  ({votes_stockham})")
print(f"Diana DeGette: {round(prct_degette*100,3)}%  ({votes_degette})")
print(f"Anthony Doane: {round(prct_doane*100,3)}%  ({votes_doane})")
print("--------------------------------------------------")
print("Winner:   " + winner)
print("--------------------------------------------------")
