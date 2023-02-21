# logs_analyzer_python

## Objective:
Logs parsing and analysis takes good amount of time. 

For troubleshooting, we spend lot of time looking at logs for some known issues, symptoms, common error messages. Idea is to develop a script, which user can quickly on the logs to uncover any known findings, which otherwise could be taking lot of time.

How to run the script?
```
bash-5.1$ python3.9 log_analyzer.py -l $log_path/log.txt -H 
============================================================================
    We found following message in the logs

    Ignoring partially flushed segment in write ahead log
    
    This typically means that we .........
    
    Check this KB for more details
    
    ============================================================================
    
    
============================================================================
    We found following message in the logs
    Number of aborted transactions not cleaned up on account of reaching size limits
    
    This typically means that we need to run compaction on offending tablets
    Check this case for more details
    
    https://xxxxxxxx.zendesk.com/agent/tickets/5416
    
    ============================================================================
    
    
Most number of logs created time period
The count of 0131 02:2 is 26231
The count of 0131 02:3 is 4432
The count of 0131 02:4 is 2522
The count of 0131 04:5 is 2672
.
.
.
``` 

