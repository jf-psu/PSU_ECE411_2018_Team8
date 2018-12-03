import pdb
#pdb.set_trace()
import sys
import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *
from tkinter import *


#serial object 
ser = serial.Serial('COM5',115200)
ser.flush()

#declare arrays values
Vv =[]
Ii=[]
plt.ion() #matplotlib to interactive node mode LIVE DATA
count = 0
window = Tk()


#def my_plot(): 
    #plt.ylim(,)#y limit

    
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
    while counter!=255:
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

    plt.title('Sensor Voltage and Current through Solar cells')
    plt.grid(True)
    plt.ylabel('Sensor Voltage V')
    plt.plot(Vv, 'b^-', label='Voltage V')   #READ DOT AND LINE
    plt.legend(loc='upper left')
    plt.show()
            
         
def clicked():
        print("Button was clicked !!")
        ser.write(str.encode('g'))
        reading_values()
 
        
                
def GUI():
        window.title("Measure Voltage and Current from Solar Pannel")
        window.geometry('900x200')
        lbl = Label(window, text="Press button to start Measuring Voltage and Current of Solar Pannel",font=("Arial Bold", 20))
        lbl.grid(column=0, row=0)
        btn = Button(window, text="Button", font=("Arial Bold", 30), command=clicked)
        btn.grid(column=0, row=3)



if __name__ == '__main__':
        GUI()
