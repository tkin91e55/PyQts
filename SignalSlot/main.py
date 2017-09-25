#Ref: http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html
import sys

from PyQt4.QtCore import QObject, pyqtSignal

class Counter(QObject):
    
    #def __init__(self):
    counter = 0

    #Declare of QtSignal: it need to connect to func(int)
    valueChangedSignal = pyqtSignal(int)

    def SetValue(self, assignVal):
    	self.counter = assignVal
    	self.valueChangedSignal.emit(assignVal)

def PrintAVal(integer):
	print 'hihi {0}'.format(integer)

if __name__ == '__main__' :
	a = Counter()
	b = Counter()

	print a.counter
	print b.counter
	print '=============='
	a.valueChangedSignal.connect(PrintAVal)
	a.valueChangedSignal.connect(b.SetValue)
	a.SetValue(3)
	print a.counter
	print b.counter
	print '=============='