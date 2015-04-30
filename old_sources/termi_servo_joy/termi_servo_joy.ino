// Programa para Placa de desarrollo del Club de Robotica, usando las libs de Arduino. Recibe vector de posiciones y genera los PWM para mover servos.
// Autor: Ignacio Carballeda 04/2014

#include <Servo.h> 

const int analogInPin0 = A0; //Analog input en pin 23 (AI O)
const int analogInPin1 = A1; //Analog input en pin 24 (AI 1)
const int analogInPin2 = A2; //Analog input en pin 25 (AI 2)
const int analogInPin3 = A3; //Analog input en pin 26 (AI 3)
const int analogInPin4 = A4; //Analog input en pin 27 (AI 4)
const int analogInPin5 = A5; //Analog input en pin 28 (AI 5)

Servo servo_0;  // Crea objetos servo
Servo servo_1;
Servo servo_2;
Servo servo_3;
Servo servo_4;
Servo servo_5;
Servo servo_6;
Servo servo_7;
Servo servo_8;
int i;
uint8_t posc[9]; //vector de posiciones
uint8_t var = 0;
int led = 17;
int sensorValue[5]; //vector de lecturas AD
uint8_t valor;    
void setup() 
{ 
    Serial.begin(115200);	//inicia
    servo_0.attach(5);  // OJO No atachear servos a RX TX u otro pin comprometido 
    servo_1.attach(6);
    servo_2.attach(7);
    servo_3.attach(8);
    servo_4.attach(13);
    servo_5.attach(12);  
    servo_6.attach(10);
    servo_7.attach(9);
    //servo_8.attach(9); 
    pinMode(led, OUTPUT);
    
} 

void loop() 
{   
    if(Serial.available()){
        valor=Serial.read();
        if(valor==200){                 //esperamos a recibir el entero 200 para saber que lo que sigue es el 1er angulo
            while (!Serial.available());
            posc[0] = Serial.read();
        }
        else if(valor==201){            //esperamos a recibir el entero 201 para saber que lo que sigue es el 2do angulo
            while (!Serial.available());
            posc[1] = Serial.read();
        }            
        else if(valor==202){            
            while (!Serial.available());
            posc[2] = Serial.read();
        }
        else if(valor==203){           
            while (!Serial.available());
            posc[3] = Serial.read();
        }
        else if(valor==204){           // .... 
            while (!Serial.available());
            posc[4] = Serial.read();
        }
        else if(valor==205){           
            while (!Serial.available());
            posc[5] = Serial.read();
        }
        else if(valor==206){            
            while (!Serial.available());
            posc[6] = Serial.read();
        }
        else if(valor==207){           
            while (!Serial.available());
            posc[7] = Serial.read();
        }
        else if(valor==208){            //esperamos a recibir el entero 208 para saber que lo que sigue es el 9no angulo
            while (!Serial.available());
            posc[8] = Serial.read();
        }
        sensorValue[0] = analogRead(analogInPin0); //Leo los pines analogicos 
        sensorValue[1] = analogRead(analogInPin1);
        sensorValue[2] = analogRead(analogInPin2); 
        sensorValue[3] = analogRead(analogInPin3); 
        sensorValue[4] = analogRead(analogInPin4); 
        sensorValue[5] = analogRead(analogInPin5);
        
        for(i=0;i<6;i++){
           while (!Serial.available());
           Serial.print("sensor=");
           Serial.print(i);
           Serial.print("/t valor=");   
           Serial.print(sensorValue[i]);
        }
        
        servo_0.write(int(posc[0]));    //se dan las instrucciones a los servos
        servo_1.write(int(posc[1]));
        servo_2.write(int(posc[2]));
        servo_3.write(int(posc[3]));
        servo_4.write(int(posc[4]));
        servo_5.write(int(posc[5]));
        servo_6.write(int(posc[6]));
        servo_7.write(int(posc[7]));
        servo_8.write(int(posc[8]));
        
          
        }        
}



    




