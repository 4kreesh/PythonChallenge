
import os
import csv

csv_path = os.path.join('.','Resources','election_data.csv') # file path to load dataset
file_to_output = os.path.join('.','Election_analysis.txt') # file path to output file to export results

t_votes =[]  
x ={} # dictionary to store the county and candidate value
c=[] # list to calculate percentage of votes each candidate won

with open(csv_path,'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    header = next(csv_reader)
    #print(header)
    
    for row in csv_reader:
        t_votes.append(row[2]) 
        if row[2] in x.keys(): # check whether the key exists already in the dictionary
            x[row[2]]=x[row[2]]+1 # increment the Values in the dictionary
        else:
            x[row[2]] = 1
            
            
total_votes = len(t_votes) 
    
with open(file_to_output,'w') as txt_file:
    output = (f'Election Results\n'
             f'--------------------------------\n'
             f'Total Votes : {total_votes}\n'
              f'--------------------------------\n'
              )
    print(output)
    txt_file.write(output)
    for key, value in x.items(): # reading through dictionary for percentage calculation
        c = round((value/total_votes * 100),3)
        voter_output = (f'{key} : {c}% ({value})\n')
        print(voter_output)
        txt_file.write(voter_output)
   
    winner = max(x, key=x.get) # finding the winning candidate with maximum votes
    result = (f'--------------------------------\n'
             f'Winner : {winner}\n'
             f'--------------------------------\n')
    print(result)
    txt_file.write(result)
    
        


# In[ ]:




