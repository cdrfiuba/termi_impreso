
import serial
nombrePuerto = '/dev/ttyUSB0'
velocidadSerial = 9600

def imprimir(vec):	
	for i in vec:
		print i
		arduino.write(str(i))

if __name__=='__main__':
	arduino = serial.Serial()
	arduino.port = nombrePuerto
	arduino.baudrate = velocidadSerial	
	arduino.open()
	vec=[1,2,3,4]
	imprimir(vec)
