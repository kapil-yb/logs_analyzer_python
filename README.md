# logs_analyzer_python

## Objective:
Logs parsing and analysis takes good amount of time. 

For troubleshooting, we spend lot of time looking at logs for some known issues, symptoms, common error messages. Idea is to develop a script, which user can quickly on the logs to uncover any known findings, which otherwise could be taking lot of time.

How to run the script?
```
bash-5.1$ ./analyzer.py --log_file_path sample.log -H
╒═══════════════╤══════════════════════════════════════════════════════════════════════════════════╤══════════════════════╤══════════════════════╤═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╕
│   Occurrences │ Message                                                                          │ First Occurrence     │ Last Occurrence      │ Troubleshooting Tips                                                                                                                                                │
╞═══════════════╪══════════════════════════════════════════════════════════════════════════════════╪══════════════════════╪══════════════════════╪═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╡
│             9 │ Rejecting Write request: Soft memory limit exceeded                              │ 0623 14:45:05.379797 │ 0623 16:45:05.725900 │ This typically means that we have overloaded system.                                                                                                                │
│               │                                                                                  │                      │                      │     Check this KB for more details: https://support.yugabyte.com/hc/en-us/articles/4403688844045-Throttling-mechanism-in-YugaByte-TServer-due-to-high-Memory-Usage- │
├───────────────┼──────────────────────────────────────────────────────────────────────────────────┼──────────────────────┼──────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│             4 │ Number of aborted transactions not cleaned up on account of reaching size limits │ 0623 14:44:05.725900 │ 0623 16:49:05.725900 │ This typically means that we need to run compaction on offending tablets                                                                                            │
│               │                                                                                  │                      │                      │     Check this case for more details                                                                                                                                │
│               │                                                                                  │                      │                      │     https://yugabyte.zendesk.com/agent/tickets/5416                                                                                                                 │
╘═══════════════╧══════════════════════════════════════════════════════════════════════════════════╧══════════════════════╧══════════════════════╧═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╛

Histogram of logs creating time period

The count of 0623 14:4 is 5
The count of 0623 16:4 is 4
The count of 0623 15:4 is 4
bash-5.1$
``` 

