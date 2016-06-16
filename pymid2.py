#!/usr/bin/env python
#coding=utf-8

from Tkinter import *
import Pmw

root = Pmw.initialise(fontScheme = 'pmw1')

counter = Pmw.Counter(
        label_text = 'Counter:',
        labelpos = 'w',
        entryfield_value = '00:00:00',
        entryfield_validate = 'time',
        datatype='time',
        increment=30,
		
)
counter.pack(fill = 'x', padx = 10, pady = 10)



combo = Pmw.ComboBox(
        label_text = 'ComboBox:',
        labelpos = 'w',
        scrolledlist_items = map(str, range(20))
)
combo.pack(fill = 'x', padx = 10, pady = 10)

Pmw.alignlabels((counter,  combo))

root.title('example')
root.mainloop()

