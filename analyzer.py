from collections import OrderedDict
import re
import tabulate

log_file_path = "sample.log"
regex_patterns = {
    "Rejecting Write request: Soft memory limit exceeded": r"Soft memory limit exceeded",
    "Number of aborted transactions not cleaned up on account of reaching size limits": r"Number of aborted transactions not cleaned up on account of reaching size limits",
    "Sample log message": r"Sample log message",
    # Add more log messages here
}
solutions = {
    "Rejecting Write request: Soft memory limit exceeded": """ This typically means that we have overloaded system.
    Check this KB for more details: https://support.yugabyte.com/hc/en-us/articles/4403688844045-Throttling-mechanism-in-YugaByte-TServer-due-to-high-Memory-Usage-""",
    "Number of aborted transactions not cleaned up on account of reaching size limits": """This typically means that we need to run compaction on offending tablets
    Check this case for more details
    https://yugabyte.zendesk.com/agent/tickets/5416""",
    "Sample log message": "Solution for Sample log message error",
    # Add more solutions here
}

with open(log_file_path, "r") as f:                                       # Open the log file
    lines = f.readlines()                                                 # Read all the lines in the log file
    results = {}                                                          # Dictionary to store the results
    for line in lines:                                                    # For each line in the log file           
        for message, pattern in regex_patterns.items():                         # For each message and pattern
            match = re.search(pattern, line)                                    # Search for the pattern in the line
            if match:                                                           # If the pattern is found in the line          
                if message not in results:                                          # If the message is not in the results dictionary, add it
                    results[message] = {                                                # Initialize the dictionary for the message
                        "num_occurrences": 0,                                               # Number of occurrences of the message
                        "first_occurrence_time": None,                                      # Time of the first occurrence of the message
                        "last_occurrence_time": None,                                       # Time of the last occurrence of the message
                        "solution": solutions[message],                                     # Solution for the message
                    }                                                                   # End of dictionary for the message            
                results[message]["num_occurrences"] += 1                            # Increment the number of occurrences of the message
                time = line.split()[0][1:] + " " + line.split()[1]                  # Get the time from the log line
                if not results[message]["first_occurrence_time"]:                   # If the first occurrence time is not set
                    results[message]["first_occurrence_time"] = time                    # set it 
                results[message]["last_occurrence_time"] = time                     # Set time as last occurrence time

    sortedDict = OrderedDict(sorted(results.items(), key=lambda x: x[1]["num_occurrences"], reverse=True))
    table = []
    for message, info in sortedDict.items():
        table.append(
            [
                info["num_occurrences"],
                message,
                info["first_occurrence_time"],
                info["last_occurrence_time"],
                info["solution"],
            ]
        )
    print(tabulate.tabulate(table, headers=["Occurrences", "Message", "First Occurrence", "Last Occurrence", "Solution"], tablefmt="simple_grid"))