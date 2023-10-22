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
   
   
#write to file
with open('analysis/results.txt', 'w') as txt_file:
    
    electionResults = ('\nElection Results\n\n----------------------------')
    print(electionResults)
    txt_file.write(electionResults)
    
    total = (f'\nTotal Votes: {voteCount}\n\n---------------------\n')
    print(total)
    txt_file.write(total)
    #for each candidate in the dictionary 
    for c in candidateVoteDict:
        
        #count of the votes for each dictionary item
        v = candidateVoteDict[c]
        #calculate the percentage of votes for this candidate against the total. 
        v_percent = float(v)/float(voteCount)*100
        
        #check if this candidate is the winner
        if v > winndingVoteCount:
            winndingVoteCount = v
            winningCandidate = c
        
        candidateLog = f'{c}: {v_percent:.3f}% ({v})\n'
        print(candidateLog)
        txt_file.write(candidateLog)

    line = '---------------------\n'
    print(line)
    txt_file.write(line)
    
    winnerLog = f'Winner: {winningCandidate}\n'
    print(winnerLog)
    txt_file.write(winnerLog)
    
    print(line)
    txt_file.write(line)
   
