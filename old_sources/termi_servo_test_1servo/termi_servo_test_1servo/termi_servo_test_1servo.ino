// Programa para Placa de desarrollo del Club de Robotica, usando las libs de Arduino. Recibe vector de posiciones y genera los PWM para mover servos.
// Autor: Ignacio Carballeda 04/2015

#include <Servo.h> 

const int analogInPin0 = A0; //Analog input en pin 23 (AI O)
Servo servo_1;  // Crea objetos servo
int j;
int sensor;
void setup() 
{ 
	Serial.begin(115200);	//inicia
	servo_1.attach(8);  // OJO No atachear servos a RX TX u otro pin comprometido 
} 

void loop() 
{   

  	sensor = analogRead(analogInPin0); //Leo los pines analogicos         
        servo_1.write(int(sensor));
	for(j=0;j<=180;j++){
		while (!Serial.available());   
		sensor = analogRead(analogInPin0); //Leo los pines analogicos         
                servo_1.write(j);
                Serial.print(sensor);
	        delay(10);	
		}
		for(j=180;j>0;j--){
		sensor = analogRead(analogInPin0); //Leo los pines analogicos         
                servo_1.write(j);
                Serial.print(sensor);			
	        delay(10);	
		}	
	                
}
