#!/usr/bin/env python
#
#	Steve Gricci - 2011
#   Python port scanner
#   Original code from: http://www.coderholic.com/python-port-scanner/ (Ben @ Coderholic)
#   Progress.py is from: http://coreygoldberg.blogspot.com/2010/01/python-command-line-progress-bar-with.html
#

from socket import *
import sys
from Con import *
from progress import ProgressBar
if __name__ == '__main__':  
	# Check that an IP/Hostname was sent
	if (len(sys.argv) != 2):
		sys.stderr.write('Usage: scanner.py <ip>')
		sys.exit(1)

	# Load Configuration
	con = Con('ports.ini');

	targetIP = gethostbyname(sys.argv[1])
	print 'Starting scan on host: ', targetIP
	p = ProgressBar(1024)
	open_ports = {}
	for i in range(1, 1024):
		p.update_time(i)
		s = socket(AF_INET, SOCK_STREAM)
		result = s.connect_ex((targetIP,i))
		s.close()
		if(result == 0):
			open_ports[str(i).rjust(5, '0')] = con.get(i);
		s.close()
	for port in sorted(open_ports.iterkeys()):
		print "Port (%s): %s" % (str(int(port)).rjust(5, ' '), open_ports[port])
