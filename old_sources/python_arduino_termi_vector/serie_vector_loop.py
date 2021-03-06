#!/usr/bin/env python

import serial
from serial import SerialException
import time

nombrePuerto = '/dev/ttyUSB1'
velocidadSerial = 19200	
posc_e=[200,0,201,0,202,0,203,0,204,0,205,0,206,0,207,0] 	#posc_e = vector de posc a enviar, se intercalan codigos de comprobacion
#indices[  ,1,   ,3,   ,5,   ,7,   ,9,  ,11,  ,13,  ,15,  ,17]
posc=[0,0,0,0,0,0,0,0] 						#posiciones de los servos
ad_vector_r=[0,0,0,0,0,0]

loop_vector_e=[1,1,1,1,1,1,1,1]
loop_vector_r=[0,0,0,0,0,0,0,0]

def indexar_vector(posc,posc_e):					#funcion que agrega indices al vector que se envia por serie
	posc_e=[200,posc[0],201,posc[1],202,posc[2],203,posc[3],204,posc[4],205,posc[5],206,posc[6],207,posc[7]]
	return posc_e

def enviar_serie(v):					#Funcion que envia el vector de posiciones por puerto serie al microcontrolador
	for i in v:				#Recorro todo el vector
		while not arduino.writable():
			pass 			#escribo solo si buffer esta disponible
		arduino.write(chr(i))
	
def leer_serie(v):				#Funcion que lee conversiones AD que envia el micro por serie
	for i in range(len(v)):
		while not arduino.readable():
			pass
		v[i]=arduino.read()
	return v

def leer_serie_mejorado(v):
	val=[0];
	for i in range(len(v)):	
		while not arduino.readable():
			pass					#Funcion que lee conversiones AD que envia el micro por serie
		if arduino.readable():
			val[0]=arduino.read()
			val[0]=map(ord,val[0])
			comp = val[0]			
			print comp
			if comp==201:
				v[1]=arduino.read()
				print "entro acaaaaaa"
			elif comp==202:
				v[3]=arduino.read()	
			elif comp==203:
				v[5]=arduino.read()
			elif comp==204:
				v[7]=arduino.read()
			elif comp==205:
				v[9]=arduino.read()
			elif comp==206:
				v[11]=arduino.read()	
	return v


def formatear(v):
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
		arduino.flush()
		arduino.flushInput()
		arduino.flushOutput()
		
	except serial.SerialException:
		print 'El puerto ya esta abierto o bien Termi desconectado.'
		quit()

	while True:
		for i in range(8):
			for j in range (180):
				posc[i]=j
				loop=indexar_vector(posc,posc_e)
				enviar_serie(loop)	
				loop_vector_r=leer_serie(loop_vector_r)
				loop_vector_r=formatear(loop_vector_r)
				print loop				
				print loop_vector_r
				time.sleep(0.02)
			
