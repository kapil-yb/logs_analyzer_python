from analyzer_dict import regex_patterns, solutions
from collections import OrderedDict
import datetime
import argparse
import tabulate
import re
import os


# Command line arguments

parser = argparse.ArgumentParser(description="Log Analyzer for YugabyteDB logs")
parser.add_argument("-l", "--log_file", required=True, nargs='+', help="Log file path")
parser.add_argument("--support-bundle", action="store_true", help="PLACEHOLDER - Analyze support bundle")
parser.add_argument("-H", "--histogram", action="store_true", help="Generate histogram graph")
parser.add_argument("-t", "--from_time", dest="start_time", help="From time in format MMDD HH:MM")
parser.add_argument("-T", "--to_time", dest="end_time", help="To time in format MMDD HH:MM")
args = parser.parse_args()

logFiles = args.log_file
start_time = datetime.datetime.strptime(args.start_time, "%m%d %H:%M") if args.start_time else None
end_time = datetime.datetime.strptime(args.end_time, "%m%d %H:%M") if args.end_time else None

def getTimeFromLog(line):
    timeFromLog = line.split(" ")[0][1:] + " " + line.split(" ")[1][:5]
    timestamp = datetime.datetime.strptime(timeFromLog, "%m%d %H:%M")
    return timestamp

def analyzeLog(logFile, start_time=None, end_time=None):
    with open(logFile, "r") as f:                                                                                                 # Open the log file
        lines = f.readlines()                                                                                                             # Read all the lines in the log file
        results = {}                                                                                                                      # Dictionary to store the results
        for line in lines:                                                                                                                # For each line in the log file           
            for message, pattern in regex_patterns.items():                                                                                     # For each message and pattern
                match = re.search(pattern, line)                                                                                                # Search for the pattern in the line
                if match and (not start_time or getTimeFromLog(line) >= start_time) and (not end_time or getTimeFromLog(line) <= end_time):     # If the pattern is found in the line and the line is within the time range          
                    if message not in results:                                                                                                     # If the message is not in the results dictionary, add it
                        results[message] = {                                                                                                           # Initialize the dictionary for the message
                            "numOccurrences": 0,                                                                                                          # Number of occurrences of the message
                            "firstOccurrenceTime": None,                                                                                                 # Time of the first occurrence of the message
                            "lastOccurrenceTime": None,                                                                                                  # Time of the last occurrence of the message
                            "solution": solutions[message],                                                                                                # Solution for the message
                        }                                                                                                                              # End of dictionary for the message            
                    results[message]["numOccurrences"] += 1                                                                                       # Increment the number of occurrences of the message
                    time = line.split()[0][1:] + " " + line.split()[1]                                                                             # Get the time from the log line
                    if not results[message]["firstOccurrenceTime"]:                                                                              # If the first occurrence time is not set
                        results[message]["firstOccurrenceTime"] = time                                                                               # set it 
                    results[message]["lastOccurrenceTime"] = time                                                                                # Set time as last occurrence time

        sortedDict = OrderedDict(sorted(results.items(), key=lambda x: x[1]["numOccurrences"], reverse=True))
        table = []
        for message, info in sortedDict.items():
            table.append(
                [
                    info["numOccurrences"],
                    message,
                    info["firstOccurrenceTime"],
                    info["lastOccurrenceTime"],
                    info["solution"],
                ]
            )
        outPutFile = logFile + "_analysis"
        open(outPutFile, "w").write(tabulate.tabulate(table, headers=["Occurrences", "Message", "First Occurrence", "Last Occurrence", "Solution"], tablefmt="simple_grid"))
        
if __name__ == "__main__":
    for logFile in logFiles:
        analyzeLog(logFile, start_time, end_time)
        