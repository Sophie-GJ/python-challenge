#Import modules needed to read csv files
import os
import csv

#Line 6 code courtesy of Tutor Kourt Bailey.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#create variables to hold information late on
candidate_list=[]
candidate_votes={}
percent_list=[]

#open and name the csv file and data within
election_data=os.path.join('..', 'Resources', 'election_data.csv')
with open(election_data) as ballot_county_candidate:
    csvreader=csv.reader(ballot_county_candidate, delimiter=',')
    csvheader=next(csvreader)

    #create starting variable for total votes
    total_votes=0

    #this loop finds the total number of votes, creates a list with candidate names, and counts the votes for the candidates
    for rownum in csvreader:
        #calculate total number of votes
        total_votes=total_votes+1
        candidate_name=rownum[2]

        #if candidate name isn't on candidate list, add it
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

            #create starting value
            candidate_votes[candidate_name]=0

        #count how many votes each candidate name on the list received
        candidate_votes[candidate_name]=candidate_votes[candidate_name]+1

    #this loop finds the candidate's percenage of votes
    for candidate in candidate_votes:

        #get specific candidate voter count alone
        #code courtesy of AskBCS Learning Assistant
        votes=candidate_votes.get(candidate)

        #find percentage
        candidate_percentage=float(votes)/float(total_votes)*100
        
        #round percentage to 3 decimal places
        rounded_percentage=round(candidate_percentage, 3)
        
        #add percentages to a list
        percent_list.append(rounded_percentage)

#Calculate the winner of the election

#Print results in terminal
print("Election Results")
print(f"Total Votes: {total_votes}")

#Export a file with results
