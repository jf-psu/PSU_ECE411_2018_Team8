
#python read from adruinoData

import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *


#serial object 
adruinoData = serial.Serial('com11',115200)

#declare arrays values
V =[]
I=[]
plt.ion() #matplotlib to interactive node mode LIVE DATA
count = 0

def my_plot(): 
	#plt.ylim(,)#y limit
	plt.title('Sensor Voltage and Current through Solar cells')
	plt.grid(True)
	plt.ylabel('Sensor Voltage V')
	plt.plot(Vv, 'b^-', label='Voltage V')   #READ DOT AND LINE
	plt.ledgend(loc='upper left')
	
	plt2=plt.twinx()
	#plt2.ylim(,)#y limit
	plt2.plot(Ii,'ro-', label='Current amp')
	plt2.set_ylabel('Current (Amp)')
	#NOT autoscale
	plt2.ticklabel_format(useOffset=False)
	plt2.legend(loc='upper right')


while True: 
	while( arduinoData.inWaiting()==0):
		pass
	
	arduinoString = adrduinoData.readline()	#read serial port
	dataArray = arduinoString.split(',')	#split into array called dataArray
	V = float(dataArray[0])					#convert value to float
	I = float(dataArray[1])
	Vv.append(V)							#Build up the array
	Ii.append(I)
	drawnow(my_plot)
	plt.pause(.000001)
	count = count +1
	if (count>50):
		Vv.pop(0)
		Ii.pop(0)
		
#https://www.youtube.com/watch?v=zH0MGNJbenc