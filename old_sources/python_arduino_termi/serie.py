#!/usr/bin/env python

import serial
import time
from numpy import interp
from serial import SerialException

nombrePuerto = '/dev/ttyUSB0'
velocidadSerial = 57600
ad_string_r="0,0,0,0,0,0"		#string de lecturas AD que se reciben del arduino
pwm_string_e=[0,0,0,0,0,0,0,0]	        #string de posiciones que se envia al arduino
ad_vector=[0,0,0,0,0,0]
posc_e=[200,0,201,0,202,0,203,0,204,0,205,0,206,0,207,0] 	#posc_e = vector de posc a enviar, se intercalan codigos de comprobacion
#indices[  ,1,   ,3,   ,5,   ,7,   ,9,  ,11,  ,13,  ,15,  ,17]
posc=[0,0,0,0,0,0,0,0]

def indexar_vector(posc,posc_e):				#funcion que agrega indices al vector que se envia por serie
	posc_e=[200,posc[0],201,posc[1],202,posc[2],203,posc[3],204,posc[4],205,posc[5],206,posc[6],207,posc[7]]
	return posc_e


def enviar_serie(v):					#Funcion que envia el vector de posiciones por puerto serie al microcontrolador
	for i in v:					#Recorro todo el vector
		if arduino.writable(): 			#escribo solo si buffer esta disponible
			arduino.write(chr(i))


def a_ddp(v):			#Traduce los valores de 0 a 1023 leidos por serie a valores de ddp [Volts]
	for i in range(len(v)-1):	
		v[i] = interp(int(v[i]),[1,1023],[0,5])
		v[i]= round(v[i],3)
	return v


def parsear_string(ad_string):	 #Parte el string que se recibe desde puerto serie.
	ad_vector=ad_string.split(',', len(ad_string))
	return ad_vector
		

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
		for i in range(8):
			for j in range(90):
				time.sleep(0.1)
				posc[i]=j
				posc_e=indexar_vector(posc,posc_e)
				enviar_serie(posc_e)
				ad_string_r = arduino.readline(); #le puse como argumento 30, o sea leer 30 bytes y tambien funciona ok
				ad_string_r = ad_string_r.split('\r', 2)		
				ad_string_r = ad_string_r[0]
				ad_vector = parsear_string(ad_string_r)
				ad_vector = a_ddp(ad_vector)		
				print posc
				print ad_vector
				print ad_string_r
			
