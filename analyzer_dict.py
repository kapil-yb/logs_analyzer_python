############################################################################################################
# Description: This file contains the dictionary of log messages and their solutions                       #
# regex_patterns is a dictionary of log messages and their regex patterns                                  #
# Where:                                                                                                    #
#   The key is the log message                                                                             #
#   The value is the regex pattern for the log message                                                     #               
# solutions is a dictionary of log messages and their solutions                                            #
# Where:                                                                                                    #  
#   The key is the log message                                                                             #
#   The value is the solution for the log message                                                          # 
# The keys in regex_patterns and solutions should be exactly the same                                      #
############################################################################################################

regex_patterns = {
    "Rejecting Write request: Soft memory limit exceeded": r"Soft memory limit exceeded",
    "Number of aborted transactions not cleaned up on account of reaching size limits": r"Number of aborted transactions not cleaned up on account of reaching size limits",
    "Long wait for safe op id": r"Long wait for safe op id",
    "Sample log message": r"Sample log message",
    # Add more log messages here
}
solutions = {
    "Rejecting Write request: Soft memory limit exceeded": """ This typically means that we have overloaded system.
    Check this KB for more details: https://support.yugabyte.com/hc/en-us/articles/4403688844045-Throttling-mechanism-in-YugaByte-TServer-due-to-high-Memory-Usage-""",
    "Number of aborted transactions not cleaned up on account of reaching size limits": """This typically means that we need to run compaction on offending tablets
    Check this case for more details
    https://yugabyte.zendesk.com/agent/tickets/5416""",
    "Long wait for safe op id": """This means that Write on disk is slow. This could be because of slow disk or load on the system.""",
    "Sample log message": "Solution for Sample log message error",
    # Add more solutions here
}