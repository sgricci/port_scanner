#!/usr/bin/env python
#
# 2011 - Steve Gricci
# Class to parse IPs passed in numerious ways
# http://www.deepcode.net/ http://www.gricci.com
#

import re

class IPParse:
	def __init__(self, ip_str):
		self.ip_str = ip_str
		return

	def parse(self):
		# Check if range calculation is necessary
		octets = self.ip_str.split('.')

		cnt = 0
		for x in octets:
			cnt += 1
			if (len(x.split('-')) > 1):
				ips = self.calc_range(octets, x, cnt)
			else:
				ips = []
				ips.append(self.ip_str)
			
		return ips

	def calc_range(self, octets, current, count):
		current = current.split('-')
		ips = []
		for x in range(int(current[0]), int(current[1])+1):
			if (count == 1):
				ips.append("%s.%s.%s.%s" % (x, octets[1], octets[2], octets[3]))
			if (count == 2):
				ips.append("%s.%s.%s.%s" % (octets[0], x, octets[2], octets[3]))
			if (count == 3):
				ips.append("%s.%s.%s.%s" % (octets[0], octets[1], x, octets[3]))
			if (count == 4):
				ips.append("%s.%s.%s.%s" % (octets[0], octets[1], octets[2], x))
		return ips
