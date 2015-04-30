// Programa para Placa de desarrollo del Club de Robotica, usando las libs de Arduino. Recibe vector de posiciones y genera los PWM para mover servos.
// Autor: Ignacio Carballeda 04/2015

#include <Servo.h> 

const int analogInPin0 = A5; //Analog input en pin 23 (AI O)
Servo servo_1;  // Crea objetos servo

int j;
int sensor;
void setup() 
{ 
	Serial.begin(9600);	//inicio
	servo_1.attach(8);  // OJO No atachear servos a RX TX u otro pin comprometido 
        Serial.println("termi is armed.");
} 

void loop() 
{   

        
  	sensor = analogRead(analogInPin0); //Leo los pines analogicos         
        servo_1.write(int(sensor));
        Serial.println("aca llego.");
	for(j=0;j<=90;j++){
		sensor = analogRead(analogInPin0); //Leo los pines analogicos         
                servo_1.write(j);
                sensor = map(sensor, 0, 1023, 0, 255);  
                Serial.println(sensor);
	        delay(20);	
		}
	for(j=90;j>0;j--){
		sensor = analogRead(analogInPin0); //Leo los pines analogicos         
                servo_1.write(j);
                sensor = map(sensor, 0, 1023, 0, 255);  
                Serial.println(sensor);
                delay(20);	
		}	
	                
}

/*
Contando desde abajo para arriba. Empezando por 1 en la base.
Terminando con 8 en la pinza.

A0 es AD servo 2  D9 es PWM
A1 es AD servo 3  D7 es PWM 
A2 es AD servo 4  D10 es PWM , ojo como esta no forzar a mas de 130, Hay que RE centrarlo.
A3 es AD servo 5  D6 es PWM
A4 es AD servo 6  D12 es PWM
         servo 7  D5 es PWM
         servo 8  D13 es PWM (pinza)

Para arreglar en HARDWARE del brazo:
Servo 7 no lee AD , A5 deberia estar conectado a el.
Servo 1 no se puede comandar D8 deberia estar conectado a el.
LED de la placa no deberia encenderse.
*/
