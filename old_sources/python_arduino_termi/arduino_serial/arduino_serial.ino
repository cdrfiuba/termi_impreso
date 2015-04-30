#include <Servo.h> 
#include <String.h>

//instancias de los objetos Servo
Servo PWM_servo_1;
Servo PWM_servo_2;
Servo PWM_servo_3;
Servo PWM_servo_4;
Servo PWM_servo_5;
Servo PWM_servo_6;
Servo PWM_servo_7;
Servo PWM_servo_8;

//conexiones de los servos
const int AD_servo_1 = A5; //revisar, este es el que no funciona 
const int AD_servo_2 = A0;
const int AD_servo_3 = A1;
const int AD_servo_4 = A2;
const int AD_servo_5 = A3;
const int AD_servo_6 = A4;

int ad_vector[8]={0,0,0,0,0,0,0,0}; //este vector contiene las lecturas de los ADs
String ad_string, pwm_string; //string que se realiza a base del vector de lecturas AD
int posc[8]={0,0,0,0,0,0,0,0}; //este vector contiene la posicion a escribir en los servos.
int i,j,p;


void setup() 
{ 
	Serial.begin(57600); //inicio conexion serie
	PWM_servo_1.attach(8);  //revisar esta conexion
        PWM_servo_2.attach(9);
        PWM_servo_3.attach(7);
        PWM_servo_4.attach(10);
        PWM_servo_5.attach(6);
        PWM_servo_6.attach(12);
        PWM_servo_7.attach(5);
        PWM_servo_8.attach(13);
} 

void loop() 
{   
  leer_AD(); //actualiza vector AD_lecturas
  escribir_PWM(); //escribe el vector posc en los objetos servo.	
  leer_string_pwm();
  concatenar_ad_string();
  Serial.println(ad_string);
}


void leer_string_pwm(){
 while(Serial.available()==0);
 pwm_string= Serial.readString();  
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
  ad_vector[0] = analogRead(AD_servo_1);
  ad_vector[1] = analogRead(AD_servo_2);
  ad_vector[2] = analogRead(AD_servo_3);
  ad_vector[3] = analogRead(AD_servo_4);
  ad_vector[4] = analogRead(AD_servo_5);
  ad_vector[5] = analogRead(AD_servo_6);
}

void concatenar_ad_string(){
    ad_string = String("<");
    for(p=0;p<5;p++){
    ad_string.concat(ad_vector[p]);
    ad_string.concat(",");
    }
    ad_string.concat(ad_vector[5]);
    ad_string.concat(">");
}

