#!/usr/bin/python


import random, time, datetime, socket
from contextlib import closing






#time.sleep(5)
#print (resultLine)






#with open('workfile') as f:
#with  open('result.log', 'a') as f:
#    f.write(result)
#f.close()

def randomLogLineLocal():
    fileSize = random.randint(100, 100000)
    dateTime = datetime.datetime(2018, random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)).strftime("%d.%m.%Y %H:%M:%S")
    resultLine = str(fileSize) + ' ' + str(dateTime) + ' [111] CMD>  cp /soso/state/ssh_104 -P 1111 root@localhost:/mnt/ftp-data/un//111111/ukr_started_on_2018-10-27-22-38.pcap /soso/ip_source/TRAFFIC/FTP/FTP-01/'+'\n' 
    print (resultLine)
    return resultLine
    
    
    
    
def randomLogLineRetrans():
    fileSize = random.randint(100, 10000)
    dateTime = datetime.datetime(2018, random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)).strftime("%d.%m.%Y %H:%M:%S")
    #dateTime = datetime.datetime(2018, random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)).strftime("%d.%m.%Y %H:%M:%S")
    resultLine = str(fileSize) + ' ' + str(dateTime) + ' [340] CMD>  cp /soso/ip_source/TRAFFIC/FTP/FTP-01/111111/222222/000-111-222 /boot/mnt/16cen/16/111111-01/18-11-11-22\n'
    print (resultLine)
    return resultLine
    
i = 0
#sock666 = socket.socket()
#sock667 = socket.socket()
#sock666.connect(('localhost', 666))
#sock667.connect(('localhost', 667))
while True:
    try:
        with closing(socket.socket()) as sock666:
	    sock666.connect(('localhost', 666))
	    sock666.send(randomLogLineLocal())
        with closing(socket.socket()) as sock667:
	    sock667.connect(('localhost', 667))
	    sock667.send(randomLogLineRetrans())
    except:
    	print ("socket error. Waiting fo 10 seconds")
    	time.sleep(10)
    time.sleep(5)
    print i
    i = i + 1
#sock666.close()
#sock667.close()


#i = 0
#while True:
#    with open('result.log', 'a') as f:
#	f.write(randomLogLine())
#	print (i)
#	i = i + 1
#	time.sleep(5)
#    f.close()




#while True:
#    print (randomLogLine())
#    time.sleep(5)
