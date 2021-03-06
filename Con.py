#!/usr/bin/env python


class Con:
	def __init__(self, file):
		self.file = file
		self.fh = open(file)
		self.buffer = self.fh.readlines()
		self.mem = {};
		self.parse()
		return

	def get(self, config_name):
		if self.mem.has_key(str(config_name)) != True: 
			return 'unknown'
		return self.mem[str(config_name)]

	def total(self):
		return len(self.mem)

	def parse(self):
		mem = dict()
		for line in self.buffer:
			sp = line.split(':')
			sp[0] = str(sp[0])
			mem[sp[0]] = sp[1].strip();

		self.mem = mem
		return
