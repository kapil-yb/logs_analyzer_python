#!/usr/bin/env python
import argparse
from histogram import *

"""
How to use?
bash-5.1$  python3.9 log_analyzer.py -l $log_path/log.txt -H
"""

parser = argparse.ArgumentParser(prog="log_analyzer.py",description='This is my help')

parser.add_argument('-l','--log_file_path', metavar='', required=True, help='Log file path')
parser.add_argument("-H",'--histogram', action="store_true",help='Generate histogram graph')
parser.add_argument("-wc",'--word_count', action="store_true",help='List top 20 word count')
parser.add_argument('-A','--ALL', action="store_true", help='FULL Health Check')
args = parser.parse_args()
LogFile=args.log_file_path

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


str2="Rejecting Write request: Soft memory limit exceeded"
str2_cnt=0
def str2_func():
   print(
    '''============================================================================
    We found following message in the logs

    '''
    + str2 +
    '''
    
    This typically means that we have overloaded system
    
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

    if args.histogram or args.ALL:
        print ("Most number of logs created time period")
        histogram(LogFile)
    if args.word_count or args.ALL:
        word_count(LogFile)

            
