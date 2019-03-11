#!/usr/bin/python3

import os
import time
import datetime

thedict = {}
sizesum = 0

def mangodump(x):
	DB_HOST = x
	BACKUP_PATH = x
	DATETIME = time.strftime('%Y%m%d-%H%M%S')
	print ("DATETIME: " + DATETIME + "\n")
	TODAYBACKUPPATH = BACKUP_PATH + DATETIME
	print (time.strftime('%Y%m%d-%H%M%S') + " - Creating TODAYBACKUPPATH '" + TODAYBACKUPPATH + "' ...")
	if not os.path.exists(TODAYBACKUPPATH):
		os.makedirs(TODAYBACKUPPATH)
	print (time.strftime('%Y%m%d-%H%M%S') + " - TODAYBACKUPPATH '" + TODAYBACKUPPATH + "' created.\n")
	print (time.strftime('%Y%m%d-%H%M%S') + " - Starting to backup database '" + DB_HOST + "' ...")
	dump_cmd = "mongodump -h " + DB_HOST + " -o " + TODAYBACKUPPATH + " --gzip"
	os.system(dump_cmd)
	print (time.strftime('%Y%m%d-%H%M%S') + " - Backup of database '" + DB_HOST + "' completed.\n")
	print (time.strftime('%Y%m%d-%H%M%S') + " - Backup script completed, your backup has been created in '" + TODAYBACKUPPATH + "' directory.\n")


with open('output.txt', 'r') as f:
	for line in f:
		key,value = line.split('\t')
		thedict[key] = value

for x in thedict.keys():
	sizesum += float(thedict[x])
	if sizesum > 5000.0:
		with open('breakdot.txt', 'a') as f2:
			f2.write(x+'\n')
		break
	else:
		try:
			mangodump(x)
		except:
			with open('exceptlist.txt', 'a') as f3:
				f3.write('except:'+x+'\n')



