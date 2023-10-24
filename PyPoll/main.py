#Import modules needed to read csv files
import os
import csv

#Line 6 code courtesy of Tutor Kourt Bailey.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#create variables to hold information late on
winning_candidate=""
winning_count=0
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
        
        #round percentage to 3 decimal places and add to a list
        rounded_percentage=round(candidate_percentage, 3)
        percent_list.append(rounded_percentage)

        #calculate winning vote count and candidate
        #code courtesy of AskBCS Learning Assistant
        #determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
      
#Print results in terminal
i=0
print("Election Results")
print(f"Total Votes: {total_votes}")
for can_name,can_votes in candidate_votes.items():
    print("Candidate Summary")
    print(can_name)
    print("Total Candidate Votes:")
    print(can_votes)
    print("Percentage of Total Votes:")
    print(percent_list[i])
    i=i+1
print(f"Winner: {winning_candidate}")

#Export a file with results
#Create, open, and write a text file 
#code courtesy of https://www.w3schools.com/python/python_file_write.asp
f=open("PyPoll_Analysis.txt", "a")
f.write("Election Analysis \n")
x=0
f.write(f"Total Votes: {total_votes} \n")
for can_name,can_votes in candidate_votes.items():
    f.write("\nCandidate Summary \n")
    f.write(can_name)
    f.write("\nTotal Candidate Votes: ")
    f.write(str(can_votes))
    f.write("\nPercentage of Total Votes: ")
    f.write(str(percent_list[x]))
    x=x+1
f.write("\nWinner: ")
f.write(str(winning_candidate))
f.close()