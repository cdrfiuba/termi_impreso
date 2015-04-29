#!/usr/bin/env python

import serial
from serial import SerialException
import time

nombrePuerto = '/dev/ttyUSB0'
velocidadSerial = 115200
ad_string="<0,0,0,0,0,0>"   #string de lecturas AD que se reciben del arduino
posc_string="<0,0,0,0,0,0,0,0>" #string de posiciones que se envia al arduino

if __name__=='__main__':
	arduino = serial.Serial()
	arduino.port = nombrePuerto
	arduino.baudrate = velocidadSerial

	try:
		arduino.open()
		#print "Termi is armed at " + time.ctime()
		#time.sleep(1)

	except serial.SerialException:
		print 'El puerto ya esta abierto o bien Termi desconectado.'
		quit()

	while True:
		
		ad_string= arduino.readline()
		print ad_string
		
		#arduino.write(ad_string)
		#loop = arduino.readline()
		#print loop


