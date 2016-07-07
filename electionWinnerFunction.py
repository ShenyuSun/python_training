'''
There are n citizens voting in this year's HackLand election. Each voter writes the name of their chosen candidate on a ballot 
and places it in a ballot box. The candidate with the highest number of votes wins the election; if two or more candidates have 
the same number of votes, then the tied candidates' names are ordered alphabetically and the last name wins.
 
Complete the electionWinnerfunction in your editor. It has 1parameter: an array of strings,votes, describing the votes in the 
ballot box. This function must review these votes and return a string representing the name of the winning candidate.
 
Input Format
The locked stub code in your editor reads the following input from stdin and passes it to your function:
The first line contains an integer,n, denoting the size of the votesarray.
Each line i of the n subsequent lines (where 0 ≤ i < n) of strings contains a citizen's vote in the form of a candidate's name.
 
Constraints
• 1 ≤ n ≤ 104
 
Output Format
Your function must return a string denoting the name of the winner. This is printed to stdout by the locked stub code in your editor.
 
Sample Input 1
10
Alex
Michael
Harry
Dave
Michael
Victor
Harry
Alex
Mary
Mary
 
Sample Output 1
Michael
 
Explanation 1
votes = {"Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"}
Alex, Harry, Michael, and Mary are all tied for the highest number of votes. Because Michael is alphabetically last, we return his name as the winner.
 
Sample Input 2
10
Victor
Veronica
Ryan
Dave
Maria
Maria
Farah
Farah
Ryan
Veronica
 
Sample Output 2
Veronica
 
Explanation 2
votes = {"Victor", "Veronica", "Ryan", "Dave", "Maria", "Maria", "Farah", "Farah", "Ryan", "Veronica"}
Veronica, Ryan, Maria, and Farah are all tied for the highest number of votes. Because Veronica is alphabetically last, we return her name as the winner.

'''
#!/bin/python3

import sys
import os

# Complete the function below.

def electionWinner(votes):
    result = {}        # Created a dictionary to store value. Example: result = {'Alex' : '1', 'Harry' : '1'}

    '''
    Loop through votes list, and if name is not in the dictionary, then create a key and its value.
    If the key is in the dictionary, then add 1 vote.
    '''
    
    for name in votes:
        if name not in result:
            result[name] = 1
        elif name in result:
            result[name] += 1
    
    '''
    Once dictionary is created, find the max value in the dictionary.
    '''
    
    maxVoteName = max(result, key=result.get)   # This find the ID that has the max value.
    maxVote = result[maxVoteName]               # This store the value to a variable called maxVote
    
    '''
    Lopp through the dictionary, and compare the value with the maxVote
    If the key value is equal to the maxVote, then add the key to willWin list
    '''
    
    willWin = []
    for winners in result:
       if result[winners] == maxVote:
           willWin.append(winners)
    
    '''
    Sort the willWin list, and then call the last value in the list.
    Return with the winner
    '''
    willWin.sort()
    theWinner = (willWin[len(willWin) - 1])
    return theWinner

f = open(os.environ['OUTPUT_PATH'], 'w')
    

_votes_cnt = 0
_votes_cnt = int(input())
_votes_i=0
_votes = []
while _votes_i < _votes_cnt:
    _votes_item = str(input())
    _votes.append(_votes_item)
    _votes_i+=1

res = electionWinner(_votes);
f.write(res + "\n")

f.close()
