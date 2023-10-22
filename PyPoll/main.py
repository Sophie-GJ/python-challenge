#Import modules needed to read csv files
import os
import csv

#Line 6 code courtesy of Tutor Kourt Bailey.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#open and name the csv file and data within
election_data=os.path.join('..', 'Resources', 'election_data.csv')
with open(election_data) as ballot_county_candidate:
    csvreader=csv.reader(ballot_county_candidate, delimiter=',')
    csvheader=next(csvreader)

#For Loop starting variable definitions
    total_votes=0
    stockham_votes=0
    degette_votes=0
    doane_votes=0
    
    for votes in csvreader:
        total_votes=total_votes+1
        candidates=[votes[2]]
        
        if candidates=candidates+1:

        
        





            
     



# #Create a list of candidates
#         if ballot==1:
#             print(previousballet)
#         elif previousballot!=ballot:
#             print(ballot[3])
    
# #Total number of votes each candidate won
# #if ballot[3] matches their name, count

# #creating variable that allows us to search for different candidate names on the ballot
# previousballot==ballot[3]

#Percentage of votes each candidate won
    #calculate individual candidate votes, create variables for each of them 
    #keep to 3 decimals?
#     stockham_percent=stockham_votes/total_votes
#     degette_percent=degette_votes/total_votes
#     doane_percent=doane_votes/total_votes
#     #create a conditional if surname_votes_total = 0 because the math will get wonky?



# #The winner of the election based on popular vote
#     #find the individual_candiate_name with greatest_individual_candidate_vote
#     winning_candidate=

# #Print results in terminal and export a text file with the results)
print("Election Results")
print(f"Total Votes: {total_votes}")
# print(f"{Individual_candidate_name}": {surname_vote_percent}" ({surname_total_votes})")
# print(f"Winner: {winning_candidate}")