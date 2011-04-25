#!/usr/bin/env python
#
#	Steve Gricci - 2011
#   Port Scanner
#   Progress.py is from: http://coreygoldberg.blogspot.com/2010/01/python-command-line-progress-bar-with.html

from socket import *
import sys
import subprocess
import re
from Con import *
from IPParse import *
from progress import ProgressBar

VERSION = '0.4.3'

def scan_port(ip, port):
	s = socket(AF_INET, SOCK_STREAM)
	setdefaulttimeout(.5)
	result = s.connect_ex((ip, port))
	s.close()
	if (result == 0):
		return True
	return False

def usage():
	if (len(sys.argv) != 2):
		sys.stderr.write('Usage: scanner.py <ip>')
		sys.exit(1)
	return True

def is_host_up(ip):
	ret = subprocess.call("ping -c 1 -t 1 %s" % ip,
			shell=True, stdout=open('/dev/null'),
			stderr=subprocess.STDOUT)
	if (ret == 0):
		return True
	return False

if __name__ == '__main__':
	# Check that an IP/Hostname was sent
	usage()
	# Load Configuration
	con = Con('ports.ini');

	targetIP = sys.argv[1]

	ipparse = IPParse(targetIP)
	ips = ipparse.parse()
	ipmatch = re.compile('(\d{1,3}\.{1}){3}\d{1,3}')
	for ip in ips:
		if (ipmatch.match(ip) == None):
			ip = gethostbyname(ip)
		# Check if the host is up first
		if (is_host_up(ip) == False):
			print "DOWN: %s is down" % ip
			continue

		print 'Starting scan on host: ', ip
		p = ProgressBar(1024)
		p.update_time(10)
		open_ports = {}
		for i in range(10, 1024):
			p.update_time(i)
			if(scan_port(ip, i)):
				# right justify for sorting
				open_ports[str(i).rjust(5, '0')] = con.get(i)

		for port in sorted(open_ports.iterkeys()):
			print "Port (%s): %s" % (str(int(port)).rjust(5, ' '), open_ports[port])
