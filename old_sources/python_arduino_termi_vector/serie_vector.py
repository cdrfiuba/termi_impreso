#!/usr/bin/env python

import serial
from serial import SerialException
import time

nombrePuerto = '/dev/ttyUSB0'
velocidadSerial = 9600
posc_e=[200,0,201,0,202,0,203,0,204,0,205,0,206,0,207,0] 	#posc_e = vector de posc a enviar, se intercalan codigos de comprobacion
#indices[  ,1,   ,3,   ,5,   ,7,   ,9,  ,11,  ,13,  ,15,  ,17]
posc=[0,0,0,0,0,0,0,0] 						#posiciones de los servos
ad_vector_r=[0,1,0,0,0,0]


def indexar_vector(posc,posc_e):				#funcion que agrega indices al vector que se envia por serie
	posc_e=[200,posc[0],201,posc[1],202,posc[2],203,posc[3],204,posc[4],205,posc[5],206,posc[6],207,posc[7]]
	return posc_e

def enviar_serie(v):					#Funcion que envia el vector de posiciones por puerto serie al microcontrolador
	for i in v:					#Recorro todo el vector
		if arduino.writable(): 			#escribo solo si buffer esta disponible
			arduino.write(chr(i))
	
def leer_serie(v):					#Funcion que lee conversiones AD que envia el micro por serie
	for i in range(len(v)):
		if arduino.writable():
			v[i]=arduino.read()
	return v

def leer_serie_mejorado(v):					#Funcion que lee conversiones AD que envia el micro por serie
	if arduino.writable():
		v[i]=arduino.read()
		vector=map(ord,v[i])
		if vector[0]==201:
			v[1]=arduino.read()
		elif vector[0]==202:
			v[3]=arduino.read()	
		elif vector[0]==203:
			v[5]=arduino.read()
		elif vector[0]==204:
			v[7]=arduino.read()
		elif vector[0]==205:
			v[9]=arduino.read()
		elif vector[0]==206:
			v[11]=arduino.read()	
	return v


def formatear(v):		#no usar , anda mal.. arreglar.
	string_v = ''.join(v)
	vector=map(ord, string_v)
	return vector


if __name__=='__main__':
	arduino = serial.Serial()
	arduino.port = nombrePuerto
	arduino.baudrate = velocidadSerial

	try:
		arduino.open()
		print "Termi is armed at " + time.ctime()
		
	except serial.SerialException:
		print 'El puerto ya esta abierto o bien Termi desconectado.'
		quit()

	while True:
		for i in range(8):
			for j in range (180):
				posc[i]=j
				posc_e=indexar_vector(posc,posc_e)
				enviar_serie(posc_e)	
				ad_vector_r=leer_serie(ad_vector_r)
				print posc_e
				print ad_vector_r

			
