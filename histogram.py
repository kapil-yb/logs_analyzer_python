# This file should generate histogram of the log file based on date and time
from collections import Counter 

def histogram(Logfile):
    d=dict() # To store the keys ( date and hours) and respective counter
    digit=['1','2','3','4','5','6','7','8','9','0'] # Want to check, if the second char in "line" is digit
    match_char=['I','W','E','F'] # Want to check for lines starting with IWEF only. Our logs are multi-line and I do not have to handle here
    with open (Logfile, 'r') as input_file:
        for line in input_file:
            if line[0] in match_char and line[1] in digit:        
                key=line[1:10] # Plan with end range, if you need to analyze on hourly basis

                if key in d: # Populating dictionary with new keys, and increment counter for existing keys
                    d[key]=d[key]+1
                else:  
                    d[key]=1

    for key in list(d.keys()):
        print("The count of {} is {}".format(key,d[key]))
    return None

def word_count(Logfile):
    count=0
    d=dict() # To store the keys ( date and hours) and respective counter
    with open (Logfile, 'r') as input_file:
        for line in input_file:
            for word in line.split():
                if word in d: # Populating dictionary with new keys, and increment counter for existing keys
                    d[word]=d[word]+1
                else:  
                    d[word]=1
                
    print ("Generating top 20 word count\n")
    top_20 = sorted(d.items(), key = lambda x:x[1], reverse = True)[:20]
    for k, v in top_20:
        print (k, v)

    return None