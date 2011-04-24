#!/usr/bin/env python
#
#  Corey Goldberg - 2010
#  ascii command-line progress bar with percentage and elapsed time display
#



import sys
import time

if sys.platform.lower().startswith('win'):
    on_windows = True
else:
    on_windows = False

class ProgressBar:
    def __init__(self, duration):
        self.duration = duration
        self.prog_bar = '[]'
        self.fill_char = '='
        self.width = 40
        self.__update_amount(0)

    def animate(self, secs):
        for i in range(secs):
            if on_windows:
                print self, '\r',
            else:
                print self, chr(27) + '[A'
            self.update_time(i + 1)
            time.sleep(1) 
        print self

    def update_time(self, elapsed_secs):
        print self, chr(27) + '[A'
        self.__update_amount((elapsed_secs / float(self.duration)) * 100.0)
        self.prog_bar += '  %d/%s' % (elapsed_secs, self.duration)

    def __update_amount(self, new_amount):
        percent_done = int(round((new_amount / 100.0) * 100.0))
        all_full = self.width - 2
        num_hashes = int(round((percent_done / 100.0) * all_full))
        self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
        pct_place = (len(self.prog_bar) / 2) - len(str(percent_done))
        pct_string = '%d%%' % percent_done
        self.prog_bar = self.prog_bar[0:pct_place] + \
            (pct_string + self.prog_bar[pct_place + len(pct_string):])

    def __str__(self):
        return str(self.prog_bar)
