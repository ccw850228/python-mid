#!/usr/bin/env python
#coding=utf-8

import Tkinter
import Pmw

def callback(tag):
    print 'Hanwei is ',tag

root = Pmw.initialise(fontScheme = 'pmw1')
root.title('Lets select')

radio = Pmw.RadioSelect(
        command = callback,
        labelpos = 'w',
        label_text = 'select:')
radio.pack(padx = 50, pady = 50)


for text in ('tall','handsome','strong'):
    radio.add(text)
#radio.invoke('tall')

exit = Tkinter.Button(text = 'Exit', command = root.destroy)
exit.pack(pady = 20)

root.mainloop()
