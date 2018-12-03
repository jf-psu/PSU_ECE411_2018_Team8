import pdb
#pdb.set_trace()
import sys
import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
from tkinter import *
from scipy.interpolate import make_interp_spline, BSpline
import time


#serial object 
ser = serial.Serial('COM5',115200)
ser.flush()

#declare arrays values
Vv =[]
Ii=[]
plt.ion() #matplotlib to interactive node mode LIVE DATA
count = 0
window = Tk()
start=0

    
  # plt2=plt.twinx()
    #plt2.ylim(,)#y limit
  #  plt2.plot(Ii,'ro-', label='Current amp')
  #  plt2.set_ylabel('Current (Amp)')
    #NOT autoscale
  #  plt2.ticklabel_format(useOffset=False)
  #  plt2.legend(loc='upper right')
  #  plt2.show()

def reading_values():
    counter=0
    global start

    plt.clf()                   #clear plot
    
   
    if(start==0):                            #creating plot first run
        plt.title('Sensor Voltage and Current through Solar cells')
        plt.grid(True)
        plt.ylabel('Values')
        plt.legend(loc='upper left')
        axes = plt.gca()
        axes.set_xlim([0,250])
        axes.set_ylim([0,50])
        start=1
    
    while counter!=250:                         #collecting 250 sample data
        arduinoString = ser.readline()
        if(arduinoString):  
            dataArray = arduinoString.split()	#split into array called dataArray
            counter=counter+1
            V = float(dataArray[0])					#convert value to float
            I = float(dataArray[1])
            Vv.append(V)							#Build up the array
            Ii.append(I)
            print(dataArray)
            counter = counter +1
    #CURVE PLOT
    #x=range(250)
    #xnew=np.linspace(0,250,100)
    #spl=make_interp_spline(Vv,Ii,k=3)
    #Vsmooth=spl(xnew)
    #plt.plot(xnew,Vsmooth')
    
    #Collected data put to graph
    plt.xlabel('samples')
    plt.plot(Vv)
    plt.plot(Ii)
    plt.legend(['Voltage V', 'Current Amp'])
    plt.show()


            
     
def clicked():                          #function when clicked    
        #wait for serial port
        #without this serial port will get unrespond
        for i in range(1,5):             #5 seconds
            print('wait for serial port in ',i,'secs') 
            time.sleep(1)
        print("Button was clicked !!")
     
        ser.write(str.encode('g'))             #sending signal
        reading_values()
 
        
#Button section            
def GUI():
        #create window
        window.title("Measure Voltage and Current from Solar Pannel")
        window.geometry('900x200')
        
        #text in window
        lbl = Label(window, text="Press button to start Measuring Voltage and Current of Solar Pannel",font=("Arial Bold", 20))
        lbl.grid(column=0, row=0)
        
        #text in button
        btn = Button(window, text="Button", font=("Arial Bold", 30), command=clicked)
        btn.grid(column=0, row=3)



if __name__ == '__main__':
        GUI()
#https://stackoverflow.com/questions/43644790/how-to-improve-the-performance-when-2d-interpolating-smoothing-lines-using-scipy
#https://stackoverflow.com/questions/46633544/smoothing-out-curve-in-python
