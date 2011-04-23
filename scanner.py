#!/usr/bin/env python
from socket import *
import sys
from Con import *
from progress import ProgressBar
if __name__ == '__main__':  
	con = Con('ports.ini');
	targetIP = gethostbyname(sys.argv[1])
	print 'Starting scan on host ', targetIP
	#scan reserved ports
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
