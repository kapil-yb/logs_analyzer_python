#!/usr/bin/env python
import argparse

"""
How to use?
bash-5.1$  python3.9 ./log_analyzer/log_analyzer.py --log_file_path="/Users/kapilmaheshwari/Downloads/yb-support-bundle-tkp-unified-oh-20230201032350.672-logs/universe_logs/tserver/logs/yb-tserver.yb-prod-cdp-api-n1.yugabyte.log.INFO.20230131-022159.10016"
"""

parser = argparse.ArgumentParser(prog="log_analyzer.py",description='This is my help')

parser.add_argument('--log_file_path',  help='Log file path')
args = parser.parse_args()
LogFile=args.log_file_path

#parser = argparse.OptionParser() # To enable command line options
#parser.add_option("-f","--file",dest="log_file_path")
#options, args = parser.parse_args()
#LogFile=options.log_file_path

str1="Number of aborted transactions not cleaned up on account of reaching size limits"
str1_cnt=0
def str1_func():
   print(
    '''============================================================================
    We found following message in the logs
    '''
    + str1 +
    '''
    
    This typically means that we need to run compaction on offending tablets
    Check this case for more details
    
    https://yugabyte.zendesk.com/agent/tickets/5416
    
    ============================================================================
    
    '''
   )


str2="Ignoring partially flushed segment in write ahead log"
str2_cnt=0
def str2_func():
   print(
    '''============================================================================
    We found following message in the logs

    '''
    + str2 +
    '''
    
    This typically means that we .........
    
    Check this KB for more details
    
    ============================================================================
    
    '''
   )

if __name__ == '__main__':
    with open(LogFile,'r') as input_file:
        for line in input_file:
            if str1 in line and str1_cnt==0:
                str1_func()
                str1_cnt=str1_cnt+1
            elif str2 in line and str2_cnt==0:
                str2_func()
                str2_cnt=str2_cnt+1
            else:
                continue


            
