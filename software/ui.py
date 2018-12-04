

from PyQt5.QtCore import Qt
from PyQt5 import QtGui  # (the example applies equally well to PySide)
import pyqtgraph as pg
import time

def collect_trace():
  trace_btn.setEnabled(False)
  app.setOverrideCursor(Qt.WaitCursor)
  print('Starting trace')
  voltage = []
  current = []
  power = []


  for i in range(0, 5):
      voltage.append(i)
      current.append(.5*(i*i))
      power.append(.5 * pow(i, 3))

      time.sleep(.5)

      #curve = plot.getPlotItem().plot()
      #plot.plot(x=voltage, y=current, clear=True, pen='b', symbol='o', symbolPen='b', symbolBrush=0.5, name='I-V')
      #plot.plot(x=voltage, y=power, pen='r', fillLevel=0, fillBrush=(255,255,255,30), name='Power')

      iv_curve.setData(x=voltage, y=current)
      power_curve.setData(x=voltage, y=power)
      #plot.plot(x=voltage, y=power, pen='r', fillLevel=0, fillBrush=(255,255,255,30), name='Power')

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
plot = pg.PlotWidget(title='Title')
plot.addLegend()
plot.setLabel('left', 'Current', units='mA')
plot.setLabel('bottom', 'Voltage', units='V')
plot.setLabel('right', 'Power', units='mW')

plot.showGrid(x=True)

# disable mouse input on plot? this doesn't work:
#plot.setMouseEnabled(x=None, y=None)

iv_curve = plot.plot([0,0], pen='b', symbol='o', symbolPen='b', symbolBrush=0.5, name='I-V')
iv_curve.clear()

power_curve = plot.plot([0,0], pen='r', fillLevel=0, fillBrush=(255,255,255,30), name='Power')
power_curve.clear()

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