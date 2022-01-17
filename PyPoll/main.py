import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidate_list = []
vote_list = []
percent_won = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_votes = total_votes + 1
        # add unique candidates to our list
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            vote_list.append(1)
        
        # if they are in list then add a vote
        else:
            index = candidate_list.index(candidate)
            vote_list[index] = vote_list[index] + 1
    print("Election Results")
    print(f"Total Votes: {total_votes}")

    # Calculate percentages and store who won
    for name in candidate_list:
        position = candidate_list.index(name)
        percent_won.append(round((vote_list[position] / total_votes) * 100, 3))
        print(f"{candidate_list[position]}: {percent_won[position]}% ({vote_list[position]})")

    # Figure out who won popular vote
    winner = vote_list[0]
    for votes in vote_list:
        if votes > winner:
            winner = votes
place = vote_list.index(winner)
print(f"Winner: {candidate_list[place]}")       

# Redoing all the print statements into output file
output_path = os.path.join("Results.csv")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(["Election Results"])
        
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    for name in candidate_list:
        position = candidate_list.index(name)
        csvwriter.writerow([f"{candidate_list[position]}: {percent_won[position]}% ({vote_list[position]})"])

    place = vote_list.index(winner)
    csvwriter.writerow([f"Winner: {candidate_list[place]}"]) 