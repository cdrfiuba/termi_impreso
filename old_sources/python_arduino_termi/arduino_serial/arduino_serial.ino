#include <Servo.h> 

Servo PWM_servo_1;
Servo PWM_servo_2;
Servo PWM_servo_3;
Servo PWM_servo_4;
Servo PWM_servo_5;
Servo PWM_servo_6;
Servo PWM_servo_7;
Servo PWM_servo_8;

const int AD_servo_1 = A5; //revisar, este es el que no funciona 
const int AD_servo_2 = A0;
const int AD_servo_3 = A1;
const int AD_servo_4 = A2;
const int AD_servo_5 = A3;
const int AD_servo_6 = A4;

int AD_lecturas[8]={0,0,0,0,0,0,0,0}; //este vector contiene las lecturas de los ADs
int posc[8]={0,0,0,0,0,0,0,0}; //este vector contiene la posicion a escribir en los servos.
int i,j,p;
char string[8];

void setup() 
{ 
	Serial.begin(9600); //inicio conexion serie
	PWM_servo_1.attach(8);  //revisar esta conexion
        PWM_servo_2.attach(9);
        PWM_servo_3.attach(7);
        PWM_servo_4.attach(10);
        PWM_servo_5.attach(6);
        PWM_servo_6.attach(12);
        PWM_servo_7.attach(5);
        PWM_servo_8.attach(13);
        //Serial.println("Termi is armed.");
} 

void loop() 
{   
  leer_AD(); //actualiza vector AD_lecturas
  escribir_PWM(); //escribe el vector posc en los objetos servo.
 	for(i=0;i<9;i++){
		for(j=0;j<=90;j++){
			posc[i]=j;
			escribir_PWM();		
			imprimir_serie();
			delay(10);	
		}
		for(j=90;j>0;j--){
			posc[i]=j;
			escribir_PWM();		
			imprimir_serie();
			delay(10);	
		}	
       }
}

void escribir_PWM(){
 PWM_servo_1.write(posc[0]);
 PWM_servo_2.write(posc[1]); 
 PWM_servo_3.write(posc[2]);  
 PWM_servo_4.write(posc[3]); 
 PWM_servo_5.write(posc[4]);
 PWM_servo_6.write(posc[5]);
 PWM_servo_7.write(posc[6]);
 PWM_servo_8.write(posc[7]); 
}

void leer_AD(){
  AD_lecturas[0] = analogRead(AD_servo_1);
  AD_lecturas[1] = analogRead(AD_servo_2);
  AD_lecturas[2] = analogRead(AD_servo_3);
  AD_lecturas[3] = analogRead(AD_servo_4);
  AD_lecturas[4] = analogRead(AD_servo_5);
  AD_lecturas[5] = analogRead(AD_servo_6);
}

void imprimir_serie(){
  for(p=0;p<9;p++){
    Serial.print(AD_lecturas[p]);
    Serial.print(" ");  
  }
  Serial.print("\t");
}
