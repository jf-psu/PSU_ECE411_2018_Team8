

from PyQt5.QtCore import Qt
from PyQt5 import QtGui  # (the example applies equally well to PySide)
import pyqtgraph as pg
import time

def collect_trace():
  trace_btn.setEnabled(False)
  app.setOverrideCursor(Qt.WaitCursor)
  print('Starting trace')
  data_x = []
  data_y = []


  for i in range(0, 5):
      data_x.append(i)
      data_y.append(.5*(i*i))
      time.sleep(.5)
      plot.plot(data_x, data_y, clear=True)
      #plot.setData(x=data_x, y=data_y)#, clear=True)
      app.processEvents()
  trace_btn.setEnabled(True)
  app.restoreOverrideCursor()



#self.timer = QtCore.QTimer()
#        self.timer.timeout.connect(self.updateplot)
#        self.timer.start(self._interval)
  #plot.addItem(y=1,x=1)
  
## Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
w = QtGui.QWidget()
w.setWindowTitle('ECE 411 Team 8 Solar Tester')
## Create some widgets to be placed inside
trace_btn = QtGui.QPushButton('&Trace')
trace_btn.clicked.connect(collect_trace)
#text = QtGui.QLineEdit('enter text')
#listw = QtGui.QListWidget()
plot = pg.PlotWidget(title='Title')
plot.setLabel('left', 'Current', units='mA')
plot.setLabel('bottom', 'Voltage', units='V')
plot.setLabel('right', 'Power', units='mW')



## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(trace_btn, 0, 0)   # button goes in upper-left
#layout.addWidget(text, 1, 0)   # text edit goes in middle-left
#layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
layout.addWidget(plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows

## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()

'''

plt = pg.plot()
plt.setWindowTitle('Solar Cell I-V Curve')
#plt.addLegend()
#l = pg.LegendItem((100,60), offset=(70,30))  # args are (size, offset)
#l.setParentItem(plt.graphicsItem())   # Note we do NOT call plt.addItem in this case

c1 = plt.plot([1,3,2,4], pen='b', symbol='o', symbolPen='b', symbolBrush=0.5, name='I-V')
c2 = plt.plot([2,1,4,3], pen='r', fillLevel=0, fillBrush=(255,255,255,30), name='Power')

plt.setLabel('left', 'Current', units='mA')
plt.setLabel('bottom', 'Voltage', units='V')
plt.setLabel('right', 'Power', units='mW')

#l.addItem(c1, 'red plot')
#l.addItem(c2, 'green plot')


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
'''