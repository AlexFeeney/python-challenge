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
    
    winningCandidate = ''
    winndingVoteCount = 0 
    
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


for c in candidateVoteDict:
    
    v = candidateVoteDict[c]
    v_percent = float(v)/float(voteCount)*100
    
    if v > winndingVoteCount:
        winndingVoteCount = v
        winningCandidate = c
    print(f'{c}: {v_percent:.3f}% ({v})\n')

print('---------------------\n')
print(f'Winner: {winningCandidate}\n')
print('---------------------\n')


#write to file
with open('analysis/results.txt', 'w') as txt_file:
    
    test = 'ok1'
    
    txt_file.write(test)