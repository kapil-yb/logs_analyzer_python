# logs_analyzer_python

## Objective:
Logs parsing and analysis takes good amount of time. 

For troubleshooting, we spend lot of time looking at logs for some known issues, symptoms, common error messages. Idea is to develop a script, which user can quickly on the logs to uncover any known findings, which otherwise could be taking lot of time.

How to run the script?
```
bash-5.1$  python3.9 ./log_analyzer/log_analyzer.py --log_file_path="<Full path to logs.txt>"
============================================================================
    We found following message in the logs

    Ignoring partially flushed segment in write ahead log
    
    This typically means that we .........
    
    Check this KB for more details
    
    ============================================================================
``` 

