#!/usr/bin/env python

import serial
from serial import SerialException

nombrePuerto = '/dev/ttyUSB1'
velocidadSerial = 57600
ad_string_r="<0,0,0,0,0,0>"		#string de lecturas AD que se reciben del arduino
pwm_string_e="<0,0,0,0,0,0,0,0>"	#string de posiciones que se envia al arduino

if __name__=='__main__':
	arduino = serial.Serial()
	arduino.port = nombrePuerto
	arduino.baudrate = velocidadSerial

	try:
		arduino.open()

	except serial.SerialException:
		print 'El puerto ya esta abierto o bien Termi desconectado.'
		quit()

	while True:
		arduino.write(pwm_string_e)
		ad_string_r = arduino.readline() #le puse como argumento 30, o sea leer 30 bytes y tambien funciona ok
		print ad_string_r


