#!/usr/bin/env python
#
#
#	Steve Gricci - 2011
#   Python port scanner
#   Original code from: http://www.coderholic.com/python-port-scanner/ (Ben @ Coderholic)
#   Progress.py is from: http://coreygoldberg.blogspot.com/2010/01/python-command-line-progress-bar-with.html

from socket import *
import sys
from Con import *
from progress import ProgressBar
if __name__ == '__main__':  
	# Load Configuration
	con = Con('ports.ini');

	targetIP = gethostbyname(sys.argv[1])
	print 'Starting scan on host: ', targetIP
	p = ProgressBar(600)
	open_ports = {}
	for i in range(1, 600):
		p.update_time(i)
		s = socket(AF_INET, SOCK_STREAM)
		result = s.connect_ex((targetIP, i))
		if(result == 0) :
			open_ports[str(i).rjust(5, '0')] = con.get(i);
		s.close()
	for port in sorted(open_ports.iterkeys()):
		print "Port (%s): %s" % (str(int(port)).rjust(5, ' '), open_ports[port])
