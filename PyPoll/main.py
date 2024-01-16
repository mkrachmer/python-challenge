# PyPoll Instructions
# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# -- The total number of votes cast
# -- A complete list of candidates who received votes
# -- The percentage of votes each candidate won
# -- The total number of votes each candidate won
# -- The winner of the election based on popular vote
# Your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

# identify dataset (includes 3 columns: "Voter ID", "County", and "Candidate")
csvpath = os.path.join('Resources', 'election_data.csv')

# initialize variables
vote_tally = 0

# create lists and dictionaries
candidates_list = {}
winner = {"name2": "", "votes": 0}

# open and read csv file
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the header row 
    csv_header = next(csvfile)  
   
    # read through each row of data after the header   
    for row in csvreader:
        # tally the total number of votes cast
        vote_tally += 1
        # apply to the respective candidate
        name = (row[2])

        if name in candidates_list:
            candidates_list[name] += 1
        else:
            candidates_list[name] = 1

    # calculate percentage of votes
    percent = {candidate: (votes / vote_tally) * 100 for candidate, votes in candidates_list.items()}
  
# determine winner       
for candidate, votes in candidates_list.items():
    if votes > winner["votes"]:
        winner["name2"] = candidate
        winner["votes"] = votes
    
# print to terminal
print("Election Results")   
print("________________________" + "\n")
print("Total Votes: " + str(vote_tally) + "\n")    
print("________________________" + "\n")
for candidate, votes in candidates_list.items():
            print(f"{candidate}: {percent[candidate]:.3f}% ({votes})")
print("________________________" + "\n")
print(f"Winner: {winner['name2']}" + "\n")
print("________________________" + "\n")

# print to new text file
output_path = os.path.join('analysis', 'challenge_analysis.csv')

with open(output_path, 'w') as textfile:
    textfile.write("Election Results" + "\n")
    textfile.write("________________________" + "\n\n")
    textfile.write("Total Votes: " + str(vote_tally) + "\n\n")
    textfile.write("________________________" + "\n\n")
    for candidate, votes in candidates_list.items():
            textfile.write(f"{candidate}: {percent[candidate]:.3f}% ({votes})" + "\n")
    textfile.write("________________________" + "\n\n")
    textfile.write(f"Winner: {winner['name2']}" + "\n")
    textfile.write("________________________" + "\n")
