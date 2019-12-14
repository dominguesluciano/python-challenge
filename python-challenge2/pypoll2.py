# import module os
import os
# Module for reading CSV files
import csv
votes_file = os.path.join('Resources', 'election_data.csv')


# The total number of votes cast: create variable for total_votes = 0 and loop through rows to sum
total_votes = 0

# A complete list of candidates who received votes
candidate_names = []

# A list of votes for each candidate
candidate_votes = []

# A list of percentages of each candidade
candidate_pct =[]


with open(votes_file, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    #loop each row to check whether candidate already existis
    for row in csvreader:
        #add up vote list
        total_votes = total_votes +1

        #declare the conditional (candidate do not exist in list)
        if row[2] not in candidate_names:
            candidate_names.append(row[2])

            #get index for new candidate
            #candidate_votes.append(0) #append to list of votes
            candidate_votes.append(1) #append to list of votes

        else:
            #get index for existing candidate
            index = candidate_names.index(row[2])
            candidate_votes[index] = candidate_votes[index]+1
    
    #loop through candidate_votes to calculate percentages
    for votes in candidate_votes:
        pct = round(votes / total_votes * 100)
        pct = "%.3f%%" % pct
        candidate_pct.append(pct) #append to list of candidates percentage

    #use same methodology of finfind index to navigate through lists
    winner_index = candidate_votes.index(max(candidate_votes))
    winner = candidate_names[winner_index]

#print everything
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidate_names[0]} {candidate_pct[0]} ({candidate_votes[0]})")
print(f"{candidate_names[1]} {candidate_pct[1]} ({candidate_votes[1]})")
print(f"{candidate_names[2]} {candidate_pct[2]} ({candidate_votes[2]})")
print(f"{candidate_names[3]} {candidate_pct[3]} ({candidate_votes[3]})")
print("-------------------------")
print(f"Winner: {winner}: {candidate_votes[winner_index]}")
print("-------------------------")
