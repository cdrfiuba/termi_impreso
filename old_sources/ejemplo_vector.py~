#!/usr/bin/env python

import serial
from serial import SerialException
import time

nombrePuerto = '/dev/ttyUSB1'
velocidadSerial = 9600

v=[0,0,0,0,0]


def leer_serie(v):					#Funcion que lee conversiones AD que envia el micro por serie
	for i in range(len(v)):
		if arduino.writable():
			v[i]=arduino.read()
	return v


if __name__=='__main__':
	arduino = serial.Serial()
	arduino.port = nombrePuerto
	arduino.baudrate = velocidadSerial

	try:
		arduino.open()
		arduino.flush()
		arduino.flushInput()
		arduino.flushOutput()
		
	except serial.SerialException:
		print 'desconectado.'
		quit()

	while True:
		#v=leer_serie(v);
		string=arduino.readline(15)
		print string
