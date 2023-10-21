import os
import csv

#credit in readme file to tutor because your paths are trash
os.chdir(os.path.dirname(os.path.realpath(__file__)))

election_data=os.path.join('..', 'Resources', 'election_data.csv')
with open(election_data) as ballot_county_candidate:
    csvreader=csv.reader(ballot_county_candidate, delimiter=',')
    csvheader=next(csvreader)

#Calculate total number of votes cast
    #do we need to worry about this containing down ballot votes as well/should i specifiy to count each unique ballot ID as 1 versus each row?
total_votes =

#Create a list of candidates who received votes
    #will need a conditional where votes > 0 for the candidate to appear
    #QUESTION: without using pandas can you create a list from the column in the csv and then remove list values where votes = 0?

#Percentage of votes each candidate won
    #calculate individual candidate votes, create variables for each of them 
    #keep to 3 decimals?
    #surname_vote_percent=surname_votes_total/total_votes
    #create a conditional if surname_votes_total = 0 because the math will get wonky?

#Total number of votes each candidate one
    #wouldn't you already have this number up above? Just run it again here? 

#The winner of the election based on popular vote
    #find the individual_candiate_name with greatest_individual_candidate_vote
    winning_candidate=

#Print results in terminal and export a text file with the results)
print("Election Results")
print(f"Total Votes:" {total_votes})
print(f'{Individual_candidate_name}": " {surname_vote_percent}" ({surname_total_votes})"')
print(f"Winner: "{winning_candidate})