#!/usr/bin/env python
import os,zipfile,sys
from datetime import datetime

def log(logfile, content):
	with open('%s.log' % logfile, 'w') as f:
		f.write('%s%s\r\n' % (time_logs(), content))
		f.close()

def time_logs():
	return '[%s]: ' % datetime.now().strftime("%Y-%m-%d %I:%M:%S")

def time():
	return datetime.now().strftime("%Y-%m-%d %I:%M:%S")


def backup(folders):
	output_folder = 'backups/%s' % time()
	try:
		os.makedirs(output_folder)
	except:
		log('backup_failure', 'Unable to create zip output folder!')
		sys.exit(1)
	for folder in folders:
		log('%s/output' % output_folder, 'Zipping up %s' % folder)
		zipfileName = "%s-%s" % (time(), folder)
		zfile = zipfile.ZipFile("%s/%s.zip" % (output_folder, zipfileName), 'w')
		for dirpath,dirs,files in os.walk(folder):
			for f in files:
				fn = os.path.join(dirpath, f)
				zfile.write(fn)

folders_to_backup = []

try:
	folders_to_backup = [x.strip() for x in open('backup_config.conf').readlines()]
except:
	log('backup_failure', 'Could not open or read backup_config.conf for reading')
	sys.exit(1)

if len(folders_to_backup) < 1:
	log('backup_failure', 'No folders specified for backup in backup_config.conf')
	sys.exit(1)

backup(folders_to_backup)