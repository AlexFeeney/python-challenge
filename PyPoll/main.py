#
#Author: @Alex Feeney
#
import csv

#open csv resoure file to read in data and store it in file_obj
with open('Resources/election_data.csv') as file_obj: 
    
    #create a reader object to read data
    readerObj = csv.reader(file_obj)
    #store header row into csvHeader
    csvHeader = next(readerObj)
    
    
    voteCount = 0 
    candidates = []
    candidateVoteDict = {}
    
    for row in readerObj: 
        
        voteCount+= 1
        
        candidate = row[2]
        
        if candidate not in candidates: 
            candidates.append(candidate)
            candidateVoteDict[candidate] = 1
        candidateVoteDict[candidate] +=1
   
   
   

print(candidates)
print(candidateVoteDict)
print(""" 
Election Results 
----------------------------    
      """)
print(f'Total Votes: {voteCount}\n')
print('---------------------')