import dateparser as dp
line="I0226 15:44:05.725900   162 mem_tracker.cc:912] Number of aborted transactions not cleaned up on account of reaching size limits"
time = dp.parse("2 pm")
print("dp time is " + time.strftime("%m%d %H:%M:%S"))
# get time by cutting the line log line
timeFromLog = line.split(" ")[0][1:] + " " + line.split(" ")[1][:5]
print("time from log is " + timeFromLog)
    
# compare the time and timeFromLog

# if timeFromLog > time.strftime("%m%d %H:%M"):
#     print("True")
# else:
#     print("False")
    
    
    
# def getTimeFromLog(line):
#     timeFromLog = line.split(" ")[0][1:] + " " + line.split(" ")[1][:8]
#     return timeFromLog



with open('log_file.txt', 'r') as log_file:
    for line in log_file:
        timestamp_str = line.split()[0]  # assuming timestamp is the first element of each line
        timestamp = datetime.datetime.strptime(timestamp_str, '%m%d %H:%M')
        
        if (not start_time or timestamp >= start_time) and (not end_time or timestamp <= end_time):
            # do something with the line, e.g. print it
            print(line.strip())